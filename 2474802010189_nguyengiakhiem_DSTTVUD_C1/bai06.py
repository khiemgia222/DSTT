import numpy as np

# Khởi tạo các lưới nguy cơ
A = np.array([[1, 1, 0, 0, 1],
              [3, 1, 0, 1, 1],
              [5, 2, 0, 1, 2],
              [2, 0, 1, 2, 3]])

B = np.array([[1, 2, 2, 1, 2],
              [2, 2, 0, 2, 0],
              [1, 0, 1, 2, 4],
              [1, 4, 1, 2, 2]])

C = np.array([[0, 5, 1, 1, 1],
              [0, 1, 1, 1, 3],
              [0, 1, 3, 4, 2],
              [0, 1, 3, 3, 0]])

D = np.array([[3, 1, 1, 0, 1],
              [5, 0, 0, 3, 7],
              [7, 0, 3, 5, 5],
              [5, 0, 3, 5, 3]])

E = np.array([[0, 0, 0, 0, 10],
              [0, 0, 0, 15, 0],
              [0, 5, 15, 5, 0],
              [20, 0, 5, 0, 0]])

# Kịch bản a: Tránh lộ bí mật (chỉ xét lưới E ≤ 5)
scenario_a = (E <= 5)

# Kịch bản b: Tránh lộ bí mật và bệnh dịch (E và D ≤ 5)
scenario_b = (E <= 5) & (D <= 5)

# Kịch bản c: Tránh mưa lũ, sạt lở, bệnh dịch, cháy rừng (B, C, D, A ≤ 5)
scenario_c = (A <= 5) & (B <= 5) & (C <= 5) & (D <= 5)

# Kịch bản d: Tất cả ≤ 5 (A, B, C, D, E)
scenario_d = (A <= 5) & (B <= 5) & (C <= 5) & (D <= 5) & (E <= 5)

# Hàm in ma trận kết quả dễ nhìn hơn
def print_scenario(name, mask):
    print(f"\n{name} (1: an toàn, 0: nguy hiểm):")
    print(mask.astype(int))

# In kết quả
print_scenario("Kịch bản a", scenario_a)
print_scenario("Kịch bản b", scenario_b)
print_scenario("Kịch bản c", scenario_c)
print_scenario("Kịch bản d", scenario_d)
