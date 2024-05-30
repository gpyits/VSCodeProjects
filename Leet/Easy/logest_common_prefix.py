# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return None.

def longest_common_prefix(string_list: list[str]) -> str:
    prefix=min(string_list, key=len)
    prefixes=[prefix]
    result=[]
    for r in range(1, len(prefix)):
        prefixes.append(prefix[:r])
    for prefix in prefixes:
        count=0
        for string in string_list:
            if prefix in string and string.index(prefix)==0:
                count+=1
                if count==len(string_list):
                    result.append(prefix)
    return max(result, key=len) if result else None

print(longest_common_prefix(["flower","flow","flight"])) #fl
print(longest_common_prefix(["dog","racecar","car"])) #None