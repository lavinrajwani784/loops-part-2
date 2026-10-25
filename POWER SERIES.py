# power_series.py
import turtle as plt

def turtle(a, n):
    """
    Generate a power series: a^0, a^1, ..., a^n
    :param a: base number (float or int)
    :param n: highest exponent (int, >= 0)
    :return: list of terms
    """
    if not isinstance(a, (int, float)):
        raise ValueError("Base 'a' must be an integer or float.")
    if not isinstance(n, int) or n < 0:
        raise ValueError("Exponent 'n' must be a non-negative integer.")

    return [a ** i for i in range(n + 1)]

def main():
    try:
        # User input
        a = float(input("Enter the base number (a): "))
        n = int(input("Enter the highest exponent (n >= 0): "))

        # Generate series
        series = power_series(a, n)

        # Display series
        print(f"Power series for a={a} up to n={n}:")
        print(series)

        # Plot series
        plt.figure(figsize=(6, 4))
        plt.plot(range(n + 1), series, marker='o', linestyle='-', color='blue')
        plt.title(f"Power Series of {a} up to n={n}")
        plt.xlabel("Exponent")
        plt.ylabel("Value")
        plt.grid(True)
        plt.show()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
