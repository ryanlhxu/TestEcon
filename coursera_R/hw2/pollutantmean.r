setwd("F:/rfiles/coursera")

pollutantmean<-function(directory, pollutant, id=1:332){
	data_name = dir(directory)
	
	# sulfate or nitrate
	index = ifelse(pollutant == "sulfate",2,3)
	
	n = length(id)
	# total observation
	count = 0
	# sum of observed pollutant 
	total = 0
	
	for(i in 1:n){
      	# acquire data path in form of£ºspecdata/001.csv
		data_path = paste(directory,data_name[id[i]],sep='/')
		
		#import the data
		data = read.table(data_path,header=T,sep=',')
		      #debug:
			#print(head(data))
            	#debug:
			#print(data[,index])
		# available observations 
		temp = !is.na(data[,index])
		
		count= count+sum(temp)
		total= total+sum(data[,index][temp])
		
}	
            return(round(total/count,3))
}

