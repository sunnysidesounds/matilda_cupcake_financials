

class LogMessages(object):
    download_files_msg = "1. Downloaded {files} with message_id: {messageId}"
    download_files_msg_error = "ERROR: No email attachments don't exist can't proceed, exiting!"
    build_model_msg = "2. Building model with data received, total records: {totalRecords} - status: {status}"
    build_model_msg_error = "ERROR: In building model with data total records: {totalRecords} - status: {status}"
    no_files_exist_msg = "ERROR: No files don't exist can't proceed, exiting!"
    filter_and_calculate_msg = "3. Calculating financials with arguments: {arguments}"
    filter_and_calculate_msg_error = "ERROR: status: {status} - total_records: {totalRecords}"
    generate_email_report_msg = "4. Sending calulated data to {toEmail} - message_id: {messageId}"
    generate_email_report_msg_error = "ERROR: No revenue could be calculated for these arguments {arguments}"
    total_revenue_msg = " - Total revenue with type: {type} - revenue: {revenue}"


class EmailMessages(object):
    revenue_row = "<p style='padding-left: 10px'> - {type} : {revenue} : {count} cookies <p/>"
    duration_period_row = "Report for period: year={year}, month={month}, week={week}"