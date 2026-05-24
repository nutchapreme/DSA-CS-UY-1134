class ClearanceList:
    def __init__(self):
        self.stack = DoublyLinkedList() #flight_id
        self.designations = ChaningHashTableMap() #key is flight_id map to gate
        
        
    def add_flight(self, flight_id, designated_gate):
        new_flight = self.stack.add_last(flight_id)
        # store a reference to the DLL NODE, not just its gate data
        self.designations[flight_id] = (new_flight, designated_gate)
        
    def next_landing(self):
        next_flight = self.stack.trailer.prev
        if next_flight is self.stack.header:
            print("No pending flights")
            return
        
        next_data = self.designations[next_flight.data]
        ret_val = (next_data[0].data, next_data[1])
        
        return ret_val
        
    def clear_for_landing(self):
        next_flight = self.stack.trailer.prev
        if next_flight is self.stack.header:
            print("No pending flights")
            return
        next_flight = self.stack.delete_last()
        flight_data = self.designations[next_flight]
        ret_val = (next_flight, flight_data[1])
        # Update this!
        del self.designations[next_flight]
        return ret_val
        
    def change_gate(flight_id, new_gate):
        if flight_id not in self.designations:
            print(f"No such flight with ID {flight_id}")
            return
        curr_flight_data = self.designations[flight_id]
        self.stack.delete_node(curr_flight_data[0])
        del self.designations[flight_id]
        
    def cancel_landing(flight_id):
        if flight_id not in self.designations:
            print(f"No such flight with ID {flight_id}")
            return
        curr_flight_data = self.designations[flight_id]
        self.stack.delete_node(curr_flihgt_data[0])
        del self.designations[flight_id]