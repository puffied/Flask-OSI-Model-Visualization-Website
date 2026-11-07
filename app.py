from flask import Flask, render_template

app = Flask(__name__)

OSI_DATA = {
    7: {"name": "Application", "desc": "This is the layer closest to the user, providing the interface for applications to access network services. It refers to the protocols software uses to communicate, such as HTTP for web browsing or SMTP for emails. This is where the user's data is created."},
    
    6: {"name": "Presentation", "desc": "This layer acts as the network's translator and formatter. It ensures data from one system is readable by another by handling formatting (e.g. JPEG, ASCII) and compression. Crucially, this layer handles encryption and decryption to secure data before transmission."},

    5: {"name": "Session", "desc": "The Session layer establishes, manages, and terminates the connections (sessions) between devices. It sets up the dialogue and handles authentication. If a connection drops, it ensures the session can be resumed where it left off, keeping data exchanges orderly."},

    4: {"name": "Transport", "desc": "This layer ensures reliable end-to-end communication. It breaks data into smaller segments and numbers them for correct reassembly. It manages flow control and error recovery by requesting lost data to be resent. It relies on protocols like reliable TCP or fast but unreliable UDP."},

    3: {"name": "Network", "desc": "The Network layer routes data across different networks to its final destination. Using logical IP addresses, it breaks data into packets and determines the best path. It relies on routers to navigate these packets through the internet from the source to the destination network."},

    2: {"name": "Data Link", "desc": "This layer ensures node-to-node transfer on the same local network. It packages raw bits into frames and uses physical MAC addresses to deliver data to the correct local device. It also handles error detection, with devices like network switches operating here."},

    1: {"name": "Physical", "desc": "The lowest layer represents the actual hardware and physical medium of the network. It transmits raw bits over cables, fiber optics, or radio waves. It defines the physical specs of the network, like voltages and cable types, forming the foundation for all other layers."},

    }

@app.route("/")
def model():
    return render_template("model.html", layers=OSI_DATA)

if __name__ == "__main__":
    app.run(debug=True)