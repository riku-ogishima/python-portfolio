# Python基礎文法の確認コード

# --- 文字列出力 ---
print("こんにちは")

# --- 数値の変数 ---
num = 1
print(num)

num1 = 123        # 整数
num2 = 1.23       # 小数
print(num1)
print(num2)

# --- 文字列の変数 ---
string_a = "こんにちは"
print(string_a)

# --- 真偽値（Boolean） ---
a = 10
b = 1
bool01 = (a < b)
print(bool01)
print(type(bool01))

# --- リスト（配列） ---
name_list = ["suzuki", "tanaka", "sasaki"]
name_list[1] = "sasaki"  # 要素の変更

print(name_list[0])
print(name_list[1])
print(name_list[2])

# --- 二次元リスト ---
group_list = [
    ["susuki", "takahashi"],
    ["tanaka", "nakamura"]
]

print(group_list[0][0])
print(group_list[0][1])
print(group_list[1][0])
print(group_list[1][1])

# --- 四則演算 ---
x = 10
y = 2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

# --- 比較演算 ---
x = 10
y = 2
z = 10

print(x < y)
print(x <= y)
print(x >= z)

print(x == y)
print(x != y)

# --- 論理演算 ---
x = 8
y = 3
print(x >= 5 and x <= 10)
print(y >= 5 and y <= 10)

x = 10
y = 2
print(x == 10 or y == 10)

