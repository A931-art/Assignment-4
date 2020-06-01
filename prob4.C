#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>


int main()
{
	int n,i;
	n=10000;
	float arr[n],p;

	FILE *fp;
	fp=fopen("prob4.txt","w");
	srand(time(0));

	for(i=0;i<n;i++)
	{
		p=rand()/((float)RAND_MAX+1);
		arr[i]=-2*log(1-p);
		fprintf(fp,"%0.6f\n",arr[i]);
	}

	fclose(fp);
}
