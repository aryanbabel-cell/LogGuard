import pandas as pd;


df = pd.read_csv("data/login_logs.txt")

print(df.head())
print(df.shape)

print("Total Records: ",len(df))
print("Successfull Login Attempts: ",(df["status"]=="SUCCESS").sum())
print("Failed Login Attempts: ",(df["status"]=="FAILED").sum())
print("Unique IP Addresses: ",(df["ip_address"].nunique()))

failed = df[df["status"] == "FAILED"]
print("Count failed attempts per IP: ")
print(failed["ip_address"].value_counts())

def classify_risk(count):
    if count>=5:
        return "HIGH"
    elif 2<=count<4:
        return "MEDIUM"
    else:
        return "LOW"

failed_counts = failed["ip_address"].value_counts()
for ip,count in failed_counts.items():    
    risk = classify_risk(count)
    print(ip,count,risk)


report = []
for ip,count in failed_counts.items():
    risk=classify_risk(count)

    report.append({
        "ip_address": ip,
        "failed_attempts": count,
        "risk_level": risk
    })


report_df = pd.DataFrame(report)

print(report_df)

report_df.to_csv("output/security_report.csv", index=False)