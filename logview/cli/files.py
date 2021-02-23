# def to_csv(syslog=SYSLOG):
#     logs = syslog.log_list
#     with open("syslog.csv", "w", newline=" ") as csvfile:
#         writer = csv.writer(csvfile, delimiter=",")
#         for log in logs:
#             writer.writerow([log.date, log.user, log.source, log.event])
#     print("Completed!")