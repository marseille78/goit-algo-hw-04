def total_salary(path: str) -> tuple|None:
    try:
        with open(path, "r", encoding="utf-8") as file:
            user_list = file.readlines()
            total_sum = 0

            for user in user_list:
                user = user.strip()
                salary = int(user.split(",")[1])
                total_sum += salary

        try:
            # return (total_sum, total_sum//len(user_list))
            return (total_sum, total_sum / len(user_list))
            # return (total_sum, total_sum / 0)
        except ZeroDivisionError:
            print("List of users is empty")
    except FileNotFoundError:
        print("File Not Found")


def main():
    try:
        file_path = "./salary_file.txt"
        print(file_path)
        total, average = total_salary(file_path)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except:
        pass


if __name__ == "__main__":
    main()