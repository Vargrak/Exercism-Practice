using System;

public class CircularBuffer<T>
{
    private T[] buffer;
    private int head;
    private int tail;
    private int count;
    private int capacity;


    public CircularBuffer(int capacity)
    {
        this.capacity = capacity;
        this.buffer = new T[capacity];
        this.head = 0;
        this.tail = 0;
        this.count = 0;    
    }

    public T Read()
    {
        if (this.count == 0)
        {
            throw new InvalidOperationException("Buffer is empty");
        }

        T value = this.buffer[this.head];
        this.head = (this.head + 1) % this.capacity;
        this.count--;
        return value;
    }

    public void Write(T value)
    {
        if (this.count == this.capacity)
        {
            throw new InvalidOperationException("Buffer is full");
        }

        this.buffer[this.tail] = value;
        this.tail = (this.tail + 1) % this.capacity;
        this.count++;
    }

    public void Overwrite(T value)
    {
        if (this.count == this.capacity)
        {
            this.head = (this.head + 1) % this.capacity;
        }
        else
        {
            this.count++;
        }

        this.buffer[this.tail] = value;
        this.tail = (this.tail + 1) % this.capacity;
    }

    public void Clear()
    {
        this.head = 0;
        this.tail = 0;
        this.count = 0;
    }
}