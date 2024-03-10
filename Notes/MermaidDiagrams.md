# Flowcharts

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

# Sequence Diagrams


```mermaid

sequenceDiagram
    participant A
    participant B
    A->>B: Message
```

# Gantt Chart

```mermaid

gantt
    title Project Timeline
    section Tasks
        Task 1:         2014-01-01, 30d
        Task 2:         2014-03-01, 15d
        Task 3:         2014-05-01, 25d
```

# Class Diagram

```mermaid

classDiagram
    class Animal {
        + name: string
        + eat(food: string): void
    }
```

# State Diagram

```mermaid

stateDiagram
    [*] --> State1
    State1 --> [*]
    State1 : this is a string
    State1 : this is another string
    State1 -> State2
    State2 --> [*]
```

# Entity Relationship Diagram

```mermaid

erDiagram
    CUSTOMER ||--o{ ORDER : places
    ORDER ||--|{ LINE-ITEM : contains
    CUSTOMER }|..|{ DELIVERY-ADDRESS : uses
```

# Pie Chart

```mermaid

pie
    title Pie Chart
    "Category 1": 40
    "Category 2": 30
    "Category 3": 20
```

# Bar Chart

```mermaid

bar
    title Bar Chart
    x-axis Label: Value
    "Category 1": 40
    "Category 2": 30
    "Category 3": 20
```

# Line Chart

```mermaid

line
    title Line Chart
    x-axis Label: Value
    y-axis Label: Value
    "Series 1":
        - x: 1, y: 10
        - x: 2, y: 20
        - x: 3, y: 15
    "Series 2":
        - x: 1, y: 15
        - x: 2, y: 10
        - x: 3, y: 25
```

# Swimlane Diagram

```mermaid

swimlaneDiagram
    lane Customer
        Customer->>Order: Submit Order
    lane Order
        Order->>Warehouse: Process Order
    lane Warehouse
        Warehouse-->>Customer: Ship Order
```
