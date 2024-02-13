import json
# import datetime

class ExampleClass:
    def __init__(self, filename):
        self.filename = filename

    def save_data(self, new_record):
        data = self.load_data()
        if data:
            updated_data = [record for record in data if not (record['name'] == new_record['name'] and record['level'] == new_record['level'])]
            updated_data.append(new_record)
        else:
            updated_data = [new_record]

        with open(self.filename, 'w') as file:
            json.dump(updated_data, file, indent=4)

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def is_record_in_data(self, name, level):
        data = self.load_data()
        return any(record['name'] == name and record['level'] == level for record in data)

    def update_or_add_record(self, new_record):
        if self.is_record_in_data(new_record['name'], new_record['level']):
            existing_data = self.load_data()
            for record in existing_data:
                if record['name'] == new_record['name'] and record['level'] == new_record['level'] and record['time'] < new_record['time']:
                    # Replace the record with the new one if 'time' is greater
                    self.save_data(new_record)
                    print(f"Updated record for {new_record['name']} (Level {new_record['level']}) with a greater 'time' value.")
                    break
            else:
                print(f"Record for {new_record['name']} (Level {new_record['level']}) already exists with a greater 'time' value.")
        else:
            # If the record doesn't exist, add the new record
            self.save_data(new_record)
            print(f"Added a new record for {new_record['name']} (Level {new_record['level']}).")

    def max_level_for_name(self, name):
        data = self.load_data()
        max_level = None

        for record in data:
            if record['name'] == name:
                if max_level is None or record['level'] > max_level:
                    max_level = record['level']

        return max_level
    
    def get_json_as_string(self):
        data = self.load_data()
        formatted_json = json.dumps(data, indent=4)  # Format JSON with indentation
        return formatted_json

    def print_json(self):
        # Print all records
        loaded_data = self.load_data()
        print("Loaded data:")
        for record in loaded_data:
            print(record)

'''
if __name__ == "__main__":
    example_instance = ExampleClass('players_data.json')


    new_record = {
            'name': 'Alice',
            'level': 1,
            'life': 100,
            'magic': 50,
            'time': 50,  # Replace with your desired time value
            'date': datetime.datetime.now().date().isoformat()
    }
    example_instance.update_or_add_record(new_record)

    new_record = {
            'name': 'Jim',
            'level': 1,
            'life': 100,
            'magic': 50,
            'time': 70,  # Replace with your desired time value
            'date': datetime.datetime.now().date().isoformat()
    }
    example_instance.update_or_add_record(new_record)

    new_record = {
            'name': 'Alice',
            'level': 2,
            'life': 100,
            'magic': 70,
            'time': 70,  # Replace with your desired time value
            'date': datetime.datetime.now().date().isoformat()
    }
    example_instance.update_or_add_record(new_record)

    new_record = {
            'name': 'Alice',
            'level': 2,
            'life': 100,
            'magic': 80,
            'time': 80,  # Replace with your desired time value
            'date': datetime.datetime.now().date().isoformat()
    }
    example_instance.update_or_add_record(new_record)
    
    example_instance.print_json()

    print("Alice's max level number:", example_instance.max_level_for_name('Alice')
'''