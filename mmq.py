import numpy as np

def main():
    xs = [0.00, 0.25, 0.50, 0.75, 1.00]
    ys = [1.00, 1.28, 1.65, 2.12, 2.72]
    m = len(xs)


    A = np.array([[m,       sum(xs)],
         [sum(xs), sum(x**2 for x in xs)]])
    B = np.array([[sum(ys)],
         [sum(xs[i] * ys[i] for i in range(m))]])
    
    print(A)
    print(B)
    

if __name__ == "__main__":
    main()