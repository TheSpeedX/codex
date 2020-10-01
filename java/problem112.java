private bool isBouncy(int number) {
 
    bool inc = false;
    bool dec = false;
 
    int last = number % 10;
    number /= 10;
 
    while (number > 0) {
        int next = number % 10;
        number /= 10;
        if (next < last)
            inc = true;
        else if (next > last)
            dec = true;
 
        last = next;
 
        if (dec && inc) return true;
    }
 
    return dec && inc;
}
