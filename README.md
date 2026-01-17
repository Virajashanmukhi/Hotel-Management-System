# 🏨 Hotel Management System (Tkinter + MySQL)

This project is a **Python Tkinter GUI based Hotel Management System** integrated with a **MySQL database** to manage hotel room availability, customer details, and billing automatically.

The application provides a simple and user-friendly interface for hotel staff to handle bookings efficiently.



## 🎯 Project Objectives

* Automate hotel room booking process
* Calculate customer bill based on stay duration
* Track available rooms in database
* Provide GUI-based interaction instead of command line
* Store and retrieve data using MySQL



## 🖥️ Application Features

* User-friendly Tkinter GUI
* Customer input form:

  * Customer Name
  * Customer ID
  * Night Stay
* Automatic bill calculation
* Real-time room availability check
* MySQL database integration
* Error handling when rooms are full
* Booking history displayed in ListBox

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* PyMySQL (Database Connectivity)
* MySQL Database

---

## 🗄️ Database Structure

Database Name: `hotel`
Table Name: `info`

| Column Name | Description               |
| ----------- | ------------------------- |
| avail_room  | Number of available rooms |
| rent        | Rent per night            |

---

## ⚙️ How It Works

1. User enters customer details.
2. System checks available rooms from database.
3. If rooms are available:

   * Bill is calculated automatically.
   * Booking details are shown in output list.
   * Available rooms are decreased by 1 in database.
4. If rooms are not available:

   * Error message is displayed.

---

## ▶️ How to Run the Project

1. Install required packages:

```bash
pip install pymysql
```

2. Create MySQL database:

```sql
CREATE DATABASE hotel;
USE hotel;

CREATE TABLE info(
    avail_room INT,
    rent INT
);
```
3. Update database credentials in code:
   
```bash
user="your_username"
passwd="your_password"
```

4. Run the Python file:

```bash
python hotel.py
```

---

## 📸 GUI Preview
<img width="1908" height="1015" alt="examplple" src="https://github.com/user-attachments/assets/c213c39f-fa75-429d-bb3d-e3f02e2518f4" />


## 🔮 Future Enhancements

* Add customer record table
* Room type selection
* Payment method integration
* Admin login system
* Booking history report export
* Room category pricing

---



