MAX_NUMBERS_ORDERED = 20


class Cart:
    """Giỏ hàng chứa tối đa MAX_NUMBERS_ORDERED đĩa DVD."""
    def sort_by_title(self):
        self.items.sort(key=lambda item: item.title)
        print("Đã sắp xếp giỏ hàng theo tiêu đề")

    def sort_by_cost(self):
        self.items.sort(key=lambda item: item.cost, reverse=True)
        print("Đã sắp xếp giỏ hàng theo giá tiền")
    def __init__(self):
        self.items = []

    def add_dvd(self, dvd):
        if len(self.items) >= MAX_NUMBERS_ORDERED:
            print("The cart is almost full")
            return False
        self.items.append(dvd)
        print(f"Đã thêm đĩa '{dvd.title}' vào giỏ hàng")
        return True

    def remove_dvd(self, dvd):
        if dvd in self.items:
            self.items.remove(dvd)
            print("The disc has been removed")
            return True
        print("The disc is not in the cart")
        return False

    def total_cost(self):
        return sum(item.cost for item in self.items)

    def print_cart(self):
        if not self.items:
            print("The cart is empty")
            return
        # (Giữ nguyên các dòng print ở dưới)
        """In chi tiết các đĩa có trong giỏ hàng theo định dạng bài thực hành."""
        print("***********************CART***********************")
        print("Ordered Items:")
        for idx, item in enumerate(self.items, 1):
            print(
                f"{idx}. DVD - {item.title} - {item.category} - {item.director} - {item.length}: {item.cost} $"
            )
        print(f"Total cost: {self.total_cost():.2f} $")
        print("***************************************************")
        