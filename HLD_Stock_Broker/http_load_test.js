import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
    vus: 100, // number of virtual users
    duration: '1m', // duration of the test
};

export default function () {
    const url = 'http://localhost:8085/placeOrder';
    const payload = JSON.stringify({
        "order_id": "order123",
        "user_id": "user1",
        "order_amount": 1500.00,
        "items": [
            {
                "stock_symbol": "AAPL",
                "order_type": "buy",
                "quantity": 10,
                "price": 150.00
            },
            {
                "stock_symbol": "GOOGL",
                "order_type": "buy",
                "quantity": 5,
                "price": 200.00
            }
        ],
        "customer_details": {
            "customer_name": "John Doe",
            "email": "johndoe@example.com",
            "phone_number": "123-456-7890",
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "Anystate",
                "country": "USA",
                "postal_code": "12345"
            }
        }
    });

    const params = {
        headers: {
            'Content-Type': 'application/json',
        },
    };

    const res = http.post(url, payload, params);

    check(res, {
        'is status 200': (r) => r.status === 200,
        'is order valid': (r) => r.status === 200 && JSON.parse(r.body).is_valid === true, // Updated validation logic
    });

    sleep(1); // Sleep for 1 second between iterations
}

// A gRPC test and an HTTP test are both methods for testing web services, but they differ in several key aspects:
// gRPC Test:

// Protocol: gRPC uses Protocol Buffers (protobuf) for serializing structured data, which is more efficient than JSON.
// Transport: It runs over HTTP/2, allowing for features like bidirectional streaming and multiplexing.
// Service definition: gRPC uses a strict contract defined in .proto files, specifying the structure of requests and responses.
// Performance: Generally faster due to binary serialization and HTTP/2.
// Language support: Strong cross-language support, as the protocol buffers generate client and server code.


// Setup: gRPC tests require generating client stubs from .proto files, while HTTP tests can be set up with standard HTTP clients.
// Data handling: gRPC tests work with strongly-typed objects, while HTTP tests often deal with JSON or form data.
// Streaming: gRPC tests can easily test streaming scenarios, which is more complex in standard HTTP.
// Headers: HTTP tests focus more on HTTP headers, while gRPC abstracts much of this away.
// Tools: HTTP testing tools are more abundant, while gRPC-specific testing tools are less common but growing.

// Would you like me to elaborate on any specific aspect of gRPC or HTTP testing?
