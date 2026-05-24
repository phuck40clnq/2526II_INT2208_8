# 2526II_INT2208_8

## Requirements

Ngân hàng CS2045 phát triển một mô-đun phần mềm để tự động ra quyết định phê duyệt các khoản vay cá nhân. Hệ thống dựa trên 4 tham số đầu vào. Nếu bất kỳ tham số nào vi phạm ràng buộc dữ liệu, hệ thống lập tức từ chối xử lý và báo lỗi "Invalid Input".

Các tham số đầu vào và Ràng buộc miền giá trị:

- age: Số nguyên. Khách hàng phải từ đủ 18 tuổi đến tối đa 65 tuổi.
- income: Số thực, làm tròn đến 1 chữ số thập phân (triệu VNĐ). Hệ thống chỉ xử lý hồ sơ nếu thu nhập nằm trong khoảng từ 5 - 500 (triệu VNĐ).
- credit_score: Số nguyên. Thang điểm chuẩn từ 300 đến 850.
- employment: Ký tự, chỉ nhận 2 giá trị: "C" (Contract - Có hợp đồng lao động) hoặc "F" (Freelance - Làm việc tự do).
- Logic nghiệp vụ: Hệ thống phân loại rủi ro tín dụng của khách hàng dựa trên credit_score như sau:
    + Từ 300 đến 500: Rủi ro cao (High)
    + Từ 501 đến 700: Rủi ro trung bình (Medium)
    + Từ 701 đến 850: Rủi ro thấp (Low)

Dựa trên income, phân loại rủi ro và employment, hệ thống sẽ xuất ra một trong ba kết quả: APPROVE (Phê duyệt), MANUAL REVIEW (Chuyển thẩm định bằng tay), hoặc REJECT (Từ chối) theo các quy tắc sau:

- Khách hàng có High Risk luôn bị REJECT, bất kể thu nhập hay việc làm.
- Khách hàng có thu nhập dưới 15.0 triệu, nếu làm tự do (Freelance) hoặc có rủi ro trung bình (Medium Risk) đều bị REJECT. Chỉ chuyển MANUAL REVIEW nếu người này có hợp đồng (Contract) và Low Risk.
- Khách hàng có thu nhập từ 15 triệu trở lên:
    + Nếu có Low Risk hoặc Medium Risk, cộng thêm việc làm là Contract -> APPROVE.
    + Nếu có Low Risk hoặc Medium Risk, nhưng làm Freelance -> MANUAL REVIEW.

--------

1. Áp dụng Phân hoạch tương đương và Phân tích giá trị biên để xác định các lớp dữ liệu hợp lệ/không hợp lệ và liệt kê các giá trị cần kiểm thử cho 3 biến age, income, credit_score.
2. Lập Bảng quyết định cho logic nghiệp vụ hợp lệ. Thực hiện rút gọn bảng để tìm ra số lượng kịch bản tối thiểu cần kiểm thử.
3. Viết danh sách các test cases hoàn chỉnh kết hợp cả giá trị biên và các quy tắc từ bảng quyết định.
4. Viết code và chứng minh rằng code đã passed qua toàn bộ test cases
