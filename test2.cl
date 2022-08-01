class Main {
    a : Int <- 1;
    b : String <- "Hola";
    c : Int <- 3; 

    main() : SELF_TYPE {
        {
            a <- a + b *c;
            self;
        }
    } ;

};