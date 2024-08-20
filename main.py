# main.py

from utils import add, multiply, average

def main():
    # 数値を定義
    num1 = 10
    num2 = 20

    # 加算と乗算の結果を表示
    sum_result = add(num1, num2)
    print(f"{num1} + {num2} = {sum_result}")

    product_result = multiply(num1, num2)
    print(f"{num1} * {num2} = {product_result}")

    # 数値のリストの平均を計算
    numbers = [1, 2, 3, 4, 5]
    avg_result = average(numbers)
    print(f"The average of {numbers} is {avg_result}")

if __name__ == "__main__":
    main()



# end of script

