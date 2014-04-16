# set work directory
setwd("F:/rfiles/coursera")

corr<-function(directory, threshold=0){
	print(threshold)
	corr = c()
	data_name = dir(directory)
	for(i in 1:332){
      	# acquire data path in form of£ºspecdata/001.csv
		data_path = paste(directory,data_name[i],sep='/')
		
		#import the data
		data = read.table(data_path,header=T,sep=',')
		    
		# available observations 
		index_sulfate = !is.na(data[,2])
		index_nitrate = !is.na(data[,3])
		
		# both observable
		index <- index_sulfate & index_nitrate
			# debug:
			# print(index)
		if(sum(index)>threshold){
			corr_new<-cor(data[,2][index],data[,3][index])
			corr=append(corr,corr_new)
			
	}
	
	}	
            #print(corr)
		if(length(corr)==0){return(corr)}
		else{return(corr)}
}
