from sklearn.preprocessing import StandardScaler

from src.utils import save_object, load_object

scaler = StandardScaler()

save_object(
    "artifacts/test.pkl",
    scaler
)

obj = load_object(
    "artifacts/test.pkl"
)

print(type(obj))