class Data:
    def __init__(self):
        self.entries = []

    def add_entry(self, name, age):
        self.entries.append({'name': name, 'age': age})

    def get_entries(self):
        return self.entries


class View:
    @staticmethod
    def display_table(entries):
        print("\nDaftar Pengguna:")
        print("{:<20} {:<10}".format("Nama", "Usia"))
        print("-" * 30)
        for entry in entries:
            print("{:<20} {:<10}".format(entry['name'], entry['age']))


class Process:
    def __init__(self):
        self.data = Data()
        self.view = View()

    def get_user_input(self):
        while True:
            try:
                name = input("Masukkan nama (atau 'exit' untuk keluar): ")
                if name.lower() == 'exit':
                    break
                age = int(input("Masukkan usia: "))
                if age < 0:
                    raise ValueError("Usia tidak boleh negatif.")
                
                self.data.add_entry(name, age)
            except ValueError as e:
                print(f"Input tidak valid: {e}")

    def display_results(self):
        entries = self.data.get_entries()
        self.view.display_table(entries)


if __name__ == "__main__":
    process = Process()
    process.get_user_input()
    process.display_results()
