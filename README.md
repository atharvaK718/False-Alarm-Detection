# False Alarm Detection System
![image](https://github.com/user-attachments/assets/935feb96-1485-4a26-9b74-d3683f774f13)

## Table of Contents
- [Introduction](#introduction)
- [Existing System](#existing-system)
- [Need for the System](#need-for-the-system)
- [Proposed System](#proposed-system)
- [Technology Used](#technology-used)
  - [Hardware Requirements](#hardware-requirements)
  - [Software Requirements](#software-requirements)
  - [Libraries](#libraries)
- [Objective](#objective)
- [Modules](#modules)
- [System Workflow](#system-workflow)
- [Data Structure](#data-structure)
  - [Admin Table](#admin-table)
  - [Train Table](#train-table)
  - [Test Table](#test-table)
  - [Maintenance Table](#maintenance-table)
  - [Report Table](#report-table)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)
- [Conclusion](#conclusion)

## Introduction

This project is designed for a chemical industry to manage H2S gas detection. The industry faced significant costs due to frequent false alarms triggered by sensors detecting H2S gas, which is hazardous to health. The system aims to reduce unnecessary sanitization processes by predicting whether an alarm is dangerous or not using a machine learning algorithm.

## Existing System

In the current setup, whenever an alarm rings, a team is called to sanitize the area, halting production and incurring costs. Most alarms are false positives, leading to unnecessary interruptions and expenses.

## Need for the System

- Reduces costs associated with the support team.
- Minimizes production halts caused by false alarms.
- Ensures the security of all employees in the chemical industry.

## Proposed System

The proposed False Alarm Detection System is a web-based solution that leverages machine learning to predict the danger level of H2S gas leaks. This helps in reducing costs and minimizing production downtime.

## Technology Used

### Hardware Requirements
- **Operating System:** Windows 10
- **RAM:** 6 GB
- **Processor:** Intel Pentium Series and above
- **Hard Disk:** 2 GB

### Software Requirements
- **IDE:** PyCharm
- **Browser:** Chrome
- **Server:** Apache HTTP server
- **Front End:** HTML5, CSS3, JavaScript, Bootstrap
- **Back End:** SQLite3
- **Editor:** Jupyter, Spyder
- **Language:** Python

### Libraries
- **Data Processing:** NumPy, Pandas
- **Visualization:** Matplotlib, Seaborn
- **Machine Learning:** Scikit-learn

## Objective

The primary objective is to automate the detection of hazardous H2S gas leaks and reduce false positives. This will save costs and time, ensuring the safety and efficiency of the production process.

## Modules

1. **Data Fetching:** Using Pandas.
2. **Data Preprocessing:**
   - Handling categorical data
   - Standard scaling
   - Checking correlation
   - Handling missing values
3. **Data Visualization:** Using Matplotlib and Seaborn.
4. **Model Training:** Using train-test split techniques.
5. **Model Evaluation:** Analyzing results using confusion matrices for various classifiers.
6. **Model Testing:** Testing on new test data.

## System Workflow

1. Data is collected from sensors.
2. Data is preprocessed and analyzed.
3. Machine learning models are trained on historical data.
4. Predictions are made in real-time when new data is received.
5. If the prediction indicates danger, the support team is alerted; otherwise, the alarm is treated as a false positive.
![image](https://github.com/user-attachments/assets/46fc3a3d-220d-44ca-a126-98d3c978d2d5)


## Data Structure

### Admin Table
| SR NO | FIELD NAME | DATA TYPE | SIZE | CONSTRAINT | DESCRIPTION |
|-------|-------------|-----------|------|------------|-------------|
| 1     | Admin_Id    | Integer   | 10   | Primary Key| Admin identification no |
| 2     | Username    | Text      | 20   | Not null   | Admin username |
| 3     | Email       | Text      | 50   | Not null   | Login email |
| 4     | Password    | Text      | 10   | Not null   | Login password |

### Train Table
| SR NO | FIELD NAME            | DATA TYPE | SIZE | CONSTRAINT | DESCRIPTION                |
|-------|------------------------|-----------|------|------------|----------------------------|
| 1     | Train_id               | Integer   | 11   | Primary Key| Unique identification      |
| 2     | Ambient temperature    | Real      | 10   | Not null   | Temperature in degree      |
| 3     | Calibration(days)      | Real      | 20   | Not null   | Calibration in days        |
| 4     | Humidity               | Integer   | 20   | Not null   | Humidity in percentage     |
| 5     | H2S content            | Integer   | 10   | Not null   | H2S gas content in ppm     |
| 6     | Detected by (% of sensor)| Integer | 10   | Not null   | Detection percentage       |
| 7     | Superiority            | Integer   | 10   | Not null   | Supporting team prediction |

### Test Table
| SR NO | FIELD NAME            | DATA TYPE | SIZE | CONSTRAINT | DESCRIPTION                |
|-------|------------------------|-----------|------|------------|----------------------------|
| 1     | Test_id                | Integer   | 11   | Primary Key| Unique identification      |
| 2     | Ambient temperature    | Real      | 10   | Not null   | Temperature in degree      |
| 3     | Calibration(days)      | Real      | 20   | Not null   | Calibration in days        |
| 4     | Humidity               | Integer   | 20   | Not null   | Humidity in percentage     |
| 5     | H2S content            | Integer   | 10   | Not null   | H2S gas content in ppm     |
| 6     | Detected by (% of sensor)| Integer | 10   | Not null   | Detection percentage       |
| 7     | Superiority Index(0/1) | Integer   | 10   | Not null   | Danger or not danger       |

### Maintenance Table
| SR NO | FIELD NAME        | DATA TYPE | SIZE | CONSTRAINT | DESCRIPTION                |
|-------|--------------------|-----------|------|------------|----------------------------|
| 1     | Mat_id             | Integer   | 11   | Primary Key| Unique identification      |
| 2     | Cases              | Integer   | 10   | Not null   | Number of cases            |
| 3     | Company name       | Text      | 20   | Not null   | Name of the company        |
| 4     | Location           | Text      | 25   | Not null   | Company location           |
| 5     | Date               | DateTime  | 10   | Not null   | Date of support team visit |
| 6     | Contact information| Text      | 50   | Not null   | Company contact details    |
| 7     | Cost               | Integer   | 30   | Not null   | Cost incurred              |

![image](https://github.com/user-attachments/assets/722dfbce-8dc8-4095-b1b4-0831bcb2b061)

### Report Table
| SR NO | FIELD NAME | DATA TYPE | SIZE | CONSTRAINT | DESCRIPTION                |
|-------|-------------|-----------|------|------------|----------------------------|
| 1     | Report_id   | Integer   | 10   | Primary Key| Unique identification      |
| 2     | Test_id     | Integer   | 11   | Foreign Key| Reference to test table    |
| 3     | Mat_id      | Integer   | 11   | Foreign Key| Reference to maintenance table |

![image](https://github.com/user-attachments/assets/fbe7eed9-0ea9-47ea-b00c-e735b8650350)


## Limitations

- The existing system has no machine learning algorithm.
- It is completely human-based, leading to frequent unnecessary costs.
- Production is paused and time is wasted during each false alarm.

## Future Enhancements

- Increase the number of parameters for more accurate results.
- Allow direct dataset uploads through the admin panel.
- Implement real-time notifications and alerts.
- Enhance the model for broader application across various industries.

## Conclusion

The False Alarm Detection System is a valuable tool for chemical industries to manage H2S gas detection efficiently. By leveraging machine learning, the system reduces costs, minimizes production downtime, and ensures the safety of all employees.
