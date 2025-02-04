import re
from collections import Counter, defaultdict
from datetime import datetime, timedelta

def parse_log_line(line):
    pattern = r'^(\S+) - - \[(\d{2})\/(\w{3})\/(\d{4}):(\d{2}):(\d{2}):(\d{2}) .*\] "(\S+) (\S+) \S+" (\d{3}) (\d+|-)'
    match = re.match(pattern, line)
    if match:
        host, day, month, year, hour, minute, second, method, url, status, size = match.groups()
        date_str = f"{day} {month} {year} {hour}:{minute}:{second}"
        date = datetime.strptime(date_str, "%d %b %Y %H:%M:%S")
        size = int(size) if size.isdigit() else 0
        return {
            "host": host,
            "date": date,
            "hour": int(hour),
            "minute": int(minute),
            "url": url,
            "status": int(status),
            "size": size,
            "method": method,
            "raw": line
        }
    return None

def process_logs(file_path):
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            parsed = parse_log_line(line)
            if parsed:
                logs.append(parsed)
    return logs

def generate_reports(logs):
    weekly_data = defaultdict(list)
    monthly_data = defaultdict(list)
    
    for log in logs:
        if log["date"].month != 8 or log["date"].year != 1995:
            continue
        week_start = log["date"] - timedelta(days=log["date"].weekday())
        if week_start.month != 8:
            week_start = datetime(1995, 8, 1)
        week_end = week_start + timedelta(days=6)
        if week_end.month != 8:
            week_end = datetime(1995, 8, 31)
        week_key = (week_start.strftime("%Y-%m-%d"), week_end.strftime("%Y-%m-%d"))
        month_key = log["date"].strftime("%Y-%m")
        
        weekly_data[week_key].append(log)
        monthly_data[month_key].append(log)
    
    return weekly_data, monthly_data

def detect_downtime(logs):
    logs.sort(key=lambda x: x["date"])
    downtime_periods = []
    downtime_hours = 0
    downtime_days = set()
    last_time = None
    
    for log in logs:
        if last_time is not None:
            gap = (log["date"] - last_time).total_seconds() / 60
            if gap > 30:
                downtime_hours += gap // 60
                downtime_periods.append(f"{last_time} to {log['date']}")
            if gap >= 1440:  # Entire day without logs
                missing_days = (log["date"].date() - last_time.date()).days - 1
                for i in range(missing_days):
                    downtime_days.add((last_time.date() + timedelta(days=i + 1)).isoformat())
        last_time = log["date"]
    
    return downtime_hours, downtime_periods, sorted(downtime_days)

def analyze_data(data, suspicious_hosts_file):
    report = []
    all_suspicious_hosts = {}
    
    for period, logs in sorted(data.items()):
        period_str = f"{period[0]} to {period[1]}" if isinstance(period, tuple) else period
        total_requests = len(logs)
        url_counter = Counter(log["url"] for log in logs)
        host_counter = Counter(log["host"] for log in logs)
        successful_requests = sum(1 for log in logs if 200 <= log["status"] < 400)
        failed_requests = sum(1 for log in logs if log["status"] >= 400)
        unusual_requests = [log["raw"] for log in logs if log["method"] not in {"GET", "POST"}]
        
        for log in logs:
            if log["method"] == "POST":
                all_suspicious_hosts[log["host"]] = "POST request"
            elif re.match(r'\d+\.\d+\.\d+\.\d+', log["host"]):
                all_suspicious_hosts[log["host"]] = "invalid domain name"
        
        downtime_hours, downtime_periods, downtime_days = detect_downtime(logs)
        
        report.append(f"Report for {period_str}")
        report.append(f"Total Requests: {total_requests}")
        report.append(f"Number of Suspicious Hosts: {len(all_suspicious_hosts)}")
        report.append("Top 10 Requested URLs:")
        for url, count in url_counter.most_common(10):
            report.append(f"  {url}: {count}")
        report.append("Top 10 Requesting Hosts:")
        for host, count in host_counter.most_common(10):
            report.append(f"  {host}: {count}")
        report.append(f"Total Successful Requests: {successful_requests}")
        report.append(f"Total Failed Requests: {failed_requests}")
        report.append(f"Unusual Requests: {len(unusual_requests)}")
        report.append(f"Total Downtime Hours: {downtime_hours}")
        report.append("Downtime Periods:")
        for period in downtime_periods:
            report.append(f"  {period}")
        report.append("-" * 40)
    
    with open(suspicious_hosts_file, "w") as f:
        for host, reason in sorted(all_suspicious_hosts.items()):
            f.write(f"{host} - {reason}\n")
    
    return "\n".join(report)

def main():
    log_file = "log.txt"
    suspicious_hosts_file = "suspicious_hosts.txt"
    logs = process_logs(log_file)
    weekly_data, monthly_data = generate_reports(logs)
    
    report_content = "Weekly Report\n" + analyze_data(weekly_data, suspicious_hosts_file)
    report_content += "\n\nMonthly Report\n" + analyze_data(monthly_data, suspicious_hosts_file)
    
    with open("report.txt", "w") as report_file:
        report_file.write(report_content)

if __name__ == "__main__":
    main()
