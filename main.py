
import csv
from datetime import datetime

# =====================================
# 1. التحقق من الأرقام
# =====================================

def get_number(message, language):
    while True:
        try:
            number = float(input(message))

            if number < 0:
                if language == "ar":
                    print("الرجاء إدخال رقم صفر أو أكبر.")
                else:
                    print("Please enter a number greater than or equal to zero.")
                continue

            return number

        except ValueError:
            if language == "ar":
                print("إدخال غير صحيح. حاول مرة أخرى.")
            else:
                print("Invalid input. Try again.")

# =====================================
# 2. دوال الحساب
# =====================================

def calculate_profit(revenue, expenses):
    return revenue - expenses

def calculate_profit_margin(revenue, profit):
    if revenue == 0:
        return None

    return (profit / revenue) * 100

def calculate_payback_period(setup_cost, monthly_profit):
    if monthly_profit <= 0:
        return None

    return setup_cost / monthly_profit

def calculate_break_even(monthly_expenses):
    # تقدير مبسط يفترض أن المصاريف ثابتة
    return monthly_expenses

# =====================================
# 3. حفظ النتائج في ملف CSV
# =====================================

def save_result(data, language):
    filename = "profit_history.csv"

    try:
        with open(filename, "a", newline="", encoding="utf-8-sig") as file:
            writer = csv.writer(file)

            if file.tell() == 0:
                writer.writerow([
                    "Date",
                    "Project",
                    "Revenue",
                    "Expenses",
                    "Setup Cost",
                    "Profit",
                    "Profit Margin",
                    "Payback Months"
                ])

            writer.writerow(data)

        if language == "ar":
            print(f"\nتم حفظ النتائج في الملف: {filename}")
        else:
            print(f"\nResults saved to: {filename}")

    except OSError:
        if language == "ar":
            print("تعذر حفظ الملف. تأكد من صلاحيات المجلد.")
        else:
            print("Could not save the file. Check folder permissions.")

# =====================================
# 4. حساب المشروع
# =====================================

def run_profit_calculator(language):
    if language == "ar":
        print("\n=== حاسبة الأرباح ===")
        project_name = input("اسم المشروع: ").strip()
        revenue = get_number("الإيرادات الشهرية بالدينار: ", language)
        expenses = get_number("المصاريف الشهرية بالدينار: ", language)
        setup_cost = get_number("تكلفة التأسيس بالدينار: ", language)
    else:
        print("\n=== Profit Calculator ===")
        project_name = input("Project name: ").strip()
        revenue = get_number("Monthly revenue (KWD): ", language)
        expenses = get_number("Monthly expenses (KWD): ", language)
        setup_cost = get_number("Setup cost (KWD): ", language)

    profit = calculate_profit(revenue, expenses)
    margin = calculate_profit_margin(revenue, profit)
    payback = calculate_payback_period(setup_cost, profit)
    break_even = calculate_break_even(expenses)

    if language == "ar":
        print("\n========== النتائج ==========")
        print(f"المشروع: {project_name or 'بدون اسم'}")
        print(f"الإيرادات الشهرية: {revenue:.2f} د.ك")
        print(f"المصاريف الشهرية: {expenses:.2f} د.ك")
        print(f"صافي الربح الشهري: {profit:.2f} د.ك")

        if margin is not None:
            print(f"هامش الربح: {margin:.2f}%")
        else:
            print("هامش الربح: غير قابل للحساب لأن الإيرادات صفر.")

        if payback is not None:
            print(f"مدة استرداد رأس المال: {payback:.1f} شهر")
        else:
            print("استرداد رأس المال: لا يمكن تقديره دون ربح شهري موجب.")

        print(f"إيرادات التعادل التقديرية: {break_even:.2f} د.ك")

        if profit > 0:
            print("حالة المشروع: ربح")
        elif profit < 0:
            print("حالة المشروع: خسارة")
        else:
            print("حالة المشروع: تعادل")

        save = input("\nهل تريد حفظ النتائج؟ (نعم/لا): ").strip().lower()
        should_save = save in ("نعم", "ن", "yes", "y")

    else:
        print("\n========== Results ==========")
        print(f"Project: {project_name or 'Unnamed'}")
        print(f"Monthly revenue: {revenue:.2f} KWD")
        print(f"Monthly expenses: {expenses:.2f} KWD")
        print(f"Monthly profit: {profit:.2f} KWD")

        if margin is not None:
            print(f"Profit margin: {margin:.2f}%")
        else:
            print("Profit margin cannot be calculated because revenue is zero.")

        if payback is not None:
            print(f"Payback period: {payback:.1f} months")
        else:
            print("Payback period requires positive monthly profit.")

        print(f"Estimated break-even revenue: {break_even:.2f} KWD")

        if profit > 0:
            print("Project status: Profit")
        elif profit < 0:
            print("Project status: Loss")
        else:
            print("Project status: Break-even")

        save = input("\nSave results? (yes/no): ").strip().lower()
        should_save = save in ("yes", "y")

    if should_save:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        data = [
            date,
            project_name,
            revenue,
            expenses,
            setup_cost,
            profit,
            margin if margin is not None else "N/A",
            payback if payback is not None else "N/A"
        ]

        save_result(data, language)

# =====================================
# 5. القائمة الرئيسية
# =====================================

def main():
    print("=" * 35)
    print("GLOBAL TOOLS | أدوات عالمية")
    print("=" * 35)

    language = input("اختر اللغة (ar/en): ").strip().lower()

    if language not in ("ar", "en"):
        language = "ar"

    while True:
        if language == "ar":
            print("\n1. حاسبة الأرباح")
            print("2. خروج")
            choice = input("اختر رقمًا: ").strip()
        else:
            print("\n1. Profit Calculator")
            print("2. Exit")
            choice = input("Choose an option: ").strip()

        if choice == "1":
            run_profit_calculator(language)

        elif choice == "2":
            if language == "ar":
                print("شكرًا لاستخدام أدواتنا!")
            else:
                print("Thank you for using our tools!")
            break

        else:
            if language == "ar":
                print("اختيار غير صحيح. حاول مرة أخرى.")
            else:
                print("Invalid choice. Try again.")

# =====================================
# 6. تشغيل البرنامج
# =====================================

if __name__ == "__main__":
    main()

