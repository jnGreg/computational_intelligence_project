from functions.gen_dist_matrix import generate_dist_matrix
from functions.task_generator import generate_task


def main():
    T = generate_task()
    generate_dist_matrix(T.points)


if __name__ == "__main__":
    main()
