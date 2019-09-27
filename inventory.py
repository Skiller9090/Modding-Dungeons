class inventory():
    def __init__(self):
        self.Items = []
        self.Item_Selected = 0
        self.Armor_Equiped = []

    def add_item(self, item):
        self.Items.append(item)

    def get_items(self):
        return self.Items

    def get_index_of_item(self, item):
        return self.Items.index(item)

    def remove_item_index(self, index):
        self.Items.pop(index)

    def remove_item(self, item):
        self.Items.pop(self.get_index_of_item(item))

    def change_item_selected(self, index):
        self.Item_Selected = index

    def get_armor(self):
        return self.Armor_Equiped

    def get_armor_index(self, item):
        return self.Armor_Equiped.index(item)

    def get_add_armor(self, item):
        self.Armor_Equiped(item)

    def remove_armor(self, item):
        self.Armor_Equiped.pop(self.get_armor_index(item))

    def remove_armor_indec(self, index):
        self.Armor_Equiped.pop(index)
