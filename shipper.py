class ShipperProcess:
    def receive_order2ship(self, product):
        invoice = f"Invoice for {product}"
        print(f"Received order2ship for {product} from Seller.")
        return invoice

    def details2buy(self, invoice):
        print(f"Send {invoice} to the Buyer.")

if __name__ == "__main__":
    shipper = ShipperProcess()

    invoice = shipper.receive_order2ship("chips")
    shipper.details2buy(invoice)