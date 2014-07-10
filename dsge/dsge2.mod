var z_1,z_2,y_1,y_2,k_1, k_2, x_1, x_2, c_1, c_2, n_1,n_2, a_1, a_2, b_1, b_2,nx_1,nx_2,ir_1,ir_2,rx_1,rx_2,p_1,p_2, w_1,w_2,r_1,r_2,qa_1,qa_2,qb_1,qb_2,lambda_1,lambda_2,f_1,f_2,yy_1,kk_1,xx_1,cc_1,aa_1,bb_1,nn_1,rr_1,yy_2,kk_2,xx_2,cc_2,aa_2,bb_2,nn_2,rr_2;
varexo eps_1, eps_2;

parameters beta, mu, gamma, theta, delta, rho, omega, A_1_1, A_1_2, A_2_1, A_2_2;

beta = 0.99;
mu   = 0.34;
gamma = -1;
theta =0.36;
delta = 0.025;
rho = -1/9;
omega = 0.85;
A_1_1=0.97;
A_1_2=0.025;
A_2_1=0.025;
A_2_2=0.97;

model;
//shock
z_1 = A_1_1 * z_1(-1) + A_1_2*z_2(-1)+eps_1;
z_2 = A_2_1 * z_1(-1) + A_2_2*z_2(-1)+eps_2;

//output
f_1=exp(z_1)*k_1(-1)^theta*n_1^(1-theta);
f_2=exp(z_2)*k_2(-1)^theta*n_2^(1-theta);

//feasibale constraint
x_1+c_1= (omega*a_1^rho+(1-omega)*b_1^rho)^(1/rho);
x_2+c_2= ((1-omega)*a_2^rho+omega*b_2^rho)^(1/rho);

// capital formation
k_1 = x_1+(1-delta)*k_1(-1);
k_2 = x_2+(1-delta)*k_2(-1);

// intermediate good
a_1+ a_2 = f_1;
b_1+ b_2 = f_2;

// wage in price of intermediate good
w_1 = (1-theta)*f_1/n_1;
w_2 = (1-theta)*f_2/n_2;

// Lagragian
lambda_1 = mu*((c_1^mu*(1-n_1)^(1-mu))^gamma)/c_1;
lambda_2 = mu*((c_2^mu*(1-n_2)^(1-mu))^gamma)/c_2;

// interest rate in price of intermediate good
r_1 =  theta*f_1/k_1(-1);
r_2 =  theta*f_2/k_2(-1);

// intermediate good pricing
qa_1 = omega*a_1^(rho-1)*((omega*a_1^rho+(1-omega)*b_1^rho)^(1/rho-1));
qb_1 = (1-omega)*b_1^(rho-1)* ((omega*a_1^rho+(1-omega)*b_1^rho)^(1/rho-1));
qa_2 = (1-omega)*a_2^(rho-1)*(((1-omega)*a_2^rho+omega*b_2^rho)^(1/rho-1));
qb_2 = omega*b_2^(rho-1)*(((1-omega)*a_2^rho+omega*b_2^rho)^(1/rho-1));

// foc to labor
(1-mu)*((c_1^mu*(1-n_1)^(1-mu))^gamma)/(1-n_1) = (lambda_1*qa_1)*w_1;
(1-mu)*((c_2^mu*(1-n_2)^(1-mu))^gamma)/(1-n_2) = (lambda_2*qb_2)*w_2;

//foc to capital
beta*lambda_1(1)*(qa_1(1) * r_1(1)+1-delta)=lambda_1;
beta*lambda_2(1)*(qb_2(1) * r_2(1)+1-delta)=lambda_2;

//foc to a_1
lambda_1* qa_1 =lambda_2* qa_2;

//foc to b_1
lambda_1* qb_1= lambda_2* qb_2;

// gdp    
y_1=qa_1*f_1;
y_2=qb_2*f_2;

//net export ratio
nx_1=(qa_1*a_2-qb_1*b_1)/y_1;
nx_2=(qb_2*b_1-qa_2*a_2)/y_2;

//import ratio
a_1*ir_1=b_1;
b_2*ir_2=a_2;

//terms of trade
qa_1*p_1=qb_1;
qb_2*p_2=qa_2;

//real exchange rate
rx_1*qa_2=qa_1;
rx_2*qa_1=qa_2;
kk_1=log(k_1);
nn_1 = log(n_1);
xx_1 =log(x_1);
cc_1=log(c_1);
aa_1=log(a_1);
bb_1=log(b_1);
rr_1 =log(r_1);
yy_1=log(y_1);
kk_2=log(k_2);
nn_2 = log(n_2);
xx_2 =log(x_2);
cc_2=log(c_2);
aa_2=log(a_2);
bb_2=log(b_2);
rr_2 =log(r_2);
yy_2=log(y_2);
end;

initval;
k_1=5.84336;
k_2=5.84336;
x_1=0.146084;
x_2=0.146084;
c_1=0.42366;
c_2=0.42366;
n_1=0.307182;
n_2=0.307182;
f_1=0.887017;
f_2=0.887017;
y_1=0.569744;
y_2=0.569744;
rx_1=1;
rx_2=1;
ir_1=0.209896;
ir_2=0.209896;
p_1=1;
p_2=1;
nx_1=1.39e-09;
nx_2=-3.30e-10;
eps_1=0;
eps_2=0;
z_1=0;
z_2=0;
a_1=0.733135;
a_2=0.153882;
b_1=0.153882;
b_2=0.733135;
w_1 =1.84806;
w_2 = 1.84806;
r_1 =  0.0546477;
r_2 =  0.0546477;
qa_1 = 0.642314;
qb_1 = 0.642314;
qa_2 = 0.642314;
qb_2 = 0.642314;
lambda_1 = 1.3692;
lambda_2 = 1.3692;
kk_1=log(k_1);
nn_1 = log(n_1);
xx_1 =log(x_1);
cc_1=log(c_1);
aa_1=log(a_1);
bb_1=log(b_1);
rr_1 =log(r_1);
yy_1=log(y_1);
kk_2=log(k_2);
nn_2 = log(n_2);
xx_2 =log(x_2);
cc_2=log(c_2);
aa_2=log(a_2);
bb_2=log(b_2);
rr_2 =log(r_2);
yy_2=log(y_2);
end;


steady;
check;

shocks;
var eps_1=0.0073^2;
var eps_2=0.0044^2;
var eps_1, eps_2= 0.29*0.0073*0.0044;
end;

stoch_simul(periods=2000,order=1,ar=10,hp_filter=1600,replic=1000,graph_format = eps);