class Nokta:
    """Düzlemdeki bir noktayı belirten sınıf. Noktanın konumu,
    nokta "çağırılarak" güncellenebilir."""

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __call__(self, x, y):
        self.x, self.y = x, y

n = Nokta(3, 4)
n(5, 8)
print(n.x, n.y)
# ve güncellendi...