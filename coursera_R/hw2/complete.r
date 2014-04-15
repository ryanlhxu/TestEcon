# set work directory
setwd("F:/rfiles/coursera")

complete<-function(directory, id){
	data_name = dir(directory)
	n = length(id)
	
	# total observations matrix
	count <- matrix(rep(0,n*2),nrow=n)
	count <- as.data.frame(count)
	colnames(count)<-c("id","nobs")
	for(i in 1:n){
      	# acquire data path in form of£ºspecdata/001.csv
		data_path = paste(directory,data_name[id[i]],sep='/')
		
		#import the data
		data = read.table(data_path,header=T,sep=',')
		    
		# available observations 
		index_sulfate = !is.na(data[,2])
		index_nitrate = !is.na(data[,3])
		
		# both observable
		index = index_sulfate & index_nitrate
			# debug:
			# print(index)
		count[i,1]=id[i]
		count[i,2]=sum(index)
	
	}	
            
		return(count)
}