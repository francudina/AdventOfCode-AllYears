
total = 0
for (pair in strsplit(readLines("input.txt"), split=",")) {

    el <- strsplit(pair, split="-")

    f <- c(el[[1]][1]:el[[1]][2])
    s <- c(el[[2]][1]:el[[2]][2])

    i <- intersect(f, s)

    total = total + if(length(i)>0) 1 else 0
}

print(paste("Total: ", total))
