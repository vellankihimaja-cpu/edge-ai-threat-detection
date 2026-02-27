import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

print("Loading dataset...")

# NSL-KDD format (no headers)
columns = [
'duration','protocol_type','service','flag','src_bytes','dst_bytes','land',
'wrong_fragment','urgent','hot','num_failed_logins','logged_in',
'num_compromised','root_shell','su_attempted','num_root','num_file_creations',
'num_shells','num_access_files','num_outbound_cmds','is_host_login',
'is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
'dst_host_same_srv_rate','dst_host_diff_srv_rate',
'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
'dst_host_serror_rate','dst_host_srv_serror_rate',
'dst_host_rerror_rate','dst_host_srv_rerror_rate','label'
]

df = pd.read_csv("data/cicids.csv", names=columns)

# Convert labels to binary
df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)

# Encode categorical features
df = pd.get_dummies(df)

X = df.drop("label", axis=1)
y = df["label"]

print("Training model...")

model = RandomForestClassifier(n_estimators=50)
model.fit(X, y)

joblib.dump(model, "edge_api/model.pkl")

print("Model trained and saved.")
