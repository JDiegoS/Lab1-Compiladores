class Main {
    a : Int <- 1 * "2";
    b : String <- "Hola";
    c : Int <- 3 - true; 

    main() : SELF_TYPE {
        {
            a <- b + 1;
            self;
        }
    } ;

};