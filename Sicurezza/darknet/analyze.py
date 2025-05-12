import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# 📂 Filenames
filename = 'data.csv'
report_file = 'report.txt'
output_dir = 'report_graphs'

# 📁 Create output directory for graphs
os.makedirs(output_dir, exist_ok=True)

# 📥 Load the data
df = pd.read_csv(filename)

# 🕒 Convert Timestamp
df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')

# 🔢 Detect numeric columns
non_numeric_cols = ['Flow ID', 'Src IP', 'Dst IP', 'Protocol', 'Timestamp', 'Label']
numeric_cols = [col for col in df.columns if col not in non_numeric_cols]
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

# 🚨 Define suspicious/illegal indicators
suspicious_labels = ['Malicious', 'Anomaly', 'Botnet', 'DDoS', 'DoS', 'Exfiltration', 'Backdoor', 'PortScan', 'Tor', 'VPN']

# 🔍 Case-insensitive keyword match for suspicious entries
df['Is Suspicious'] = df['Label'].astype(str).str.contains('|'.join(suspicious_labels), case=False, na=False)

# 📝 Write textual report
with open(report_file, 'w') as f:
    f.write("=== 📊 Network Traffic Log Report ===\n\n")
    f.write(f"🧾 Total Entries: {len(df)}\n")
    f.write(f"🧾 Total Columns: {len(df.columns)}\n\n")

    f.write("=== 🧬 Column Overview ===\n")
    for col in df.columns:
        dtype = df[col].dtype
        nulls = df[col].isnull().sum()
        unique = df[col].nunique()
        f.write(f"- {col} (type: {dtype}) | Missing: {nulls} | Unique: {unique}\n")
    f.write("\n")

    f.write("=== 📈 Numeric Statistics ===\n")
    f.write(df[numeric_cols].describe().transpose().to_string())
    f.write("\n\n")

    if df['Timestamp'].notnull().any():
        f.write("=== ⏱️ Timestamp Range ===\n")
        f.write(f"Start: {df['Timestamp'].min()}\n")
        f.write(f"End  : {df['Timestamp'].max()}\n\n")

    if 'Protocol' in df.columns:
        f.write("=== 🧪 Protocol Distribution ===\n")
        f.write(df['Protocol'].value_counts().to_string())
        f.write("\n\n")

    if 'Label' in df.columns:
        f.write("=== 🏷️ Label Distribution ===\n")
        f.write(df['Label'].value_counts().to_string())
        f.write("\n\n")

    if 'Src IP' in df.columns and 'Dst IP' in df.columns:
        f.write("=== 🌐 Top 5 Source IPs ===\n")
        f.write(df['Src IP'].value_counts().head().to_string())
        f.write("\n\n")

        f.write("=== 🎯 Top 5 Destination IPs ===\n")
        f.write(df['Dst IP'].value_counts().head().to_string())
        f.write("\n\n")

    # ⚠️ Suspicious Activity Summary
    f.write("=== 🚨 Suspicious Activity Summary ===\n")
    total_suspicious = df['Is Suspicious'].sum()
    suspicious_percent = (total_suspicious / len(df)) * 100
    f.write(f"Total Suspicious Entries: {total_suspicious} ({suspicious_percent:.2f}%)\n")
    f.write("Criteria: Entries labeled with any of the following keywords:\n")
    f.write(", ".join(suspicious_labels) + "\n\n")

    if 'Label' in df.columns:
        suspicious_counts = df[df['Is Suspicious']]['Label'].value_counts()
        if not suspicious_counts.empty:
            f.write("Breakdown by Suspicious Labels:\n")
            f.write(suspicious_counts.to_string())
        else:
            f.write("No suspicious entries found.\n")
    f.write("\n")

# 📊 Plot settings
sns.set(style="whitegrid")

# 1. Protocol Usage
if 'Protocol' in df.columns:
    plt.figure(figsize=(6, 4))
    df['Protocol'].value_counts().plot(kind='bar', color='skyblue')
    plt.title("📡 Protocol Usage")
    plt.xlabel("Protocol")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'protocol_usage.png'))
    plt.close()

# 2. Label Distribution
if 'Label' in df.columns:
    plt.figure(figsize=(6, 4))
    df['Label'].value_counts().plot(kind='bar', color='lightgreen')
    plt.title("🏷️ Label Distribution")
    plt.xlabel("Label")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'label_distribution.png'))
    plt.close()

# 3. Top Source IPs
if 'Src IP' in df.columns:
    plt.figure(figsize=(6, 4))
    df['Src IP'].value_counts().head(5).plot(kind='bar', color='salmon')
    plt.title("🌐 Top 5 Source IPs")
    plt.xlabel("Source IP")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'top_src_ips.png'))
    plt.close()

# 4. Flow Duration Histogram
if 'Flow Duration' in df.columns:
    plt.figure(figsize=(6, 4))
    df['Flow Duration'].dropna().clip(upper=df['Flow Duration'].quantile(0.99)).hist(bins=50, color='orange')
    plt.title("⏳ Flow Duration Distribution")
    plt.xlabel("Flow Duration")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'flow_duration_histogram.png'))
    plt.close()

# 5. Suspicious Traffic by Label
if 'Label' in df.columns:
    plt.figure(figsize=(8, 5))
    label_counts = df['Label'].value_counts()
    colors = ['red' if label in suspicious_labels else 'green' for label in label_counts.index]

    label_counts.plot(kind='bar', color=colors)
    plt.title("🚦 Potentially Suspicious Traffic by Label")
    plt.xlabel("Label")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'suspicious_traffic_by_label.png'))
    plt.close()

# ✅ Final message
print(f"✅ Report written to '{report_file}' and 📊 graphs saved in '{output_dir}'")
