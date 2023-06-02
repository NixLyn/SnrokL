

<style>
    body {
    	height: 100vh;
	    --sz: 7px; /*** size ***/
    	--c0: #020202;
    	--c1: #171b1f;
        --c2: #333333;
        --c3: #00ff0095;
        --ts: 50%/ calc(var(--sz) * 16.8) calc(var(--sz) * 22);
        background:
		/*bottom*/
        conic-gradient(from 120deg at 50% 86.5%, var(--c1) 0 120deg, #fff0 0 360deg) var(--ts),
        conic-gradient(from 120deg at 50% 86.5%, var(--c1) 0 120deg, #fff0 0 360deg) var(--ts),
		/*bottom dark*/
		conic-gradient(from 120deg at 50% 74%, var(--c0) 0 120deg, #fff0 0 360deg) var(--ts),
		/*right*/
		conic-gradient(from 60deg at 60% 50%, var(--c1) 0 60deg, var(--c2) 0 120deg, #fff0 0 360deg) var(--ts),
		/*left*/
		conic-gradient(from 180deg at 40% 50%, var(--c3) 0 60deg, var(--c1) 0 120deg, #fff0 0 360deg) var(--ts),
		/*top dark*/
        conic-gradient(from 0deg at 90% 35%, var(--c0) 0 90deg, #fff0 0 360deg) var(--ts),
        conic-gradient(from -90deg at 10% 35%, var(--c0) 0 90deg, #fff0 0 360deg) var(--ts),
        conic-gradient(from 0deg at 90% 35%, var(--c0) 0 90deg, #fff0 0 360deg) var(--ts),
        conic-gradient(from -90deg at 10% 35%, var(--c0) 0 90deg, #fff0 0 360deg) var(--ts),
	    	/*top*/
        conic-gradient(from -60deg at 50% 13.5%, var(--c1) 0 120deg, #fff0 0 360deg) var(--ts),
        conic-gradient(from -60deg at 50% 13.5%, var(--c1) 0 120deg, #fff0 0 360deg) var(--ts),
		conic-gradient(from -60deg at 50% 41%, var(--c2) 0 60deg, var(--c3) 0 120deg, #fff0 0 360deg) var(--ts),
		var(--c0) ;
    }


    p {
        font-size: medium;
    }



    .da-head {
        margin-top: -15px;
        margin-left: -40%;
        margin-right: -10%;
        width: 100wv;
        height: fit-content;
        padding-left: 20%; 
        padding-right: 15%;
        padding-top: 1px;
        padding-bottom: 10px;
        border-radius: 20px;
        background-color: #111111F5;
        color: white;
        box-shadow: 10px 8px 10px 5px #00ff00;

    }

    .midspan  {
        margin-top: 10px;
        margin-left: -40%;
        margin-right: -10%;
        width: 90wv;
        height: 90wv;
        padding-left: 25%; 
        padding-right: 10%;
        padding-top: 5px;
        padding-bottom: 5px;
        border-radius: 20px;
        background-color: #111111F7;
        color: white;
        box-shadow: 10px 8px 10px 5px #00ff00;

    }
    .code_it {
        font-size: small;
        padding-top: 5px;
        padding-bottom: 5px;
        padding-left: 15px; 
        width: 80wv;
        right: 5vw; 
        height: fit-content;
        padding: 5px 80wv; 
        background-color: black; /* linear-gradient(-45deg, #9834eb, #e73c7e, #23a6d5, #23d5ab); ; */
        color: white;
        border-radius: 20px;
    }
    .code_it *{
        font-size: 13px;
        margin-right: 15px;
    }

    .segment {
        display: box;
        width: 80wv;
        right: 5vw; 
        height: fit-content;
        padding: 5px 80wv; 
        background-color: black; 
        color: #00ff00F2;
        border-radius: 5px;
        padding-left: 2px; 
        padding-top: 0;
        padding-bottom: 1px;
        font-size: small;


    }

    .tb_sh_0 {
        width: 70vw;
        background: linear-gradient(-45deg, #9834eb, #e73c7e, #23a6d5, #23d5ab);
        border-radius: 15px;
        padding-top: 5px;
        padding-bottom: 5px;
        border-top-left-radius: 8em;
        overflow-y: hidden;
        overflow-x: hidden;
    }


    .tb_box {
        margin-left: 1%;
        margin-right: 1%;
        padding-top: 1%;
        padding-bottom: 1%;

        width: 98%;
        height: calc(fit-content + 5px);
        background-color: black;
        border-radius: 14px;
        display: block;
        border-top-left-radius: 20em;
    }
    .tb_box *{
        font-size: small;
    }

    .tb_box_1 {
        margin-left: 1%;
        margin-right: 1%;
        padding-top: 1%;
        padding-bottom: 1%;

        width: 98%;
        height: calc(fit-content + 5px);
        background-color: black;
        border-radius: 14px;
        display: block;
        border-top-left-radius: 10em;
    }
    .tb_box_1 *{
        font-size: small;
    }

    .tb_sh_1 {
        margin-left: -21px;
        width: 80vw;
        background: linear-gradient(-45deg, #9834eb, #e73c7e, #23a6d5, #23d5ab);
        border-radius: 10px;
        padding-top: 2px;
        padding-bottom: 2px;
    }

    .snippet{
        padding-left: 0%;
        margin-right: 2px;
        margin-left: 1px;
        padding-top: 1px;
        margin-top: 1px;
        width: 100%;
        height: fit-content;
        background-color: black;
        border-radius: 12px;

    }
    .snippet img {
        border-radius: 12px;
    }


    li {
        margin-left: -15px;
        font-size: small;
        list-style-type: none; 
        color: #00ff00;

        }

    .tb_sh_2 {
        margin-left: -21px;
        width: 80vw;
        background: linear-gradient(-45deg, #9834eb, #e73c7e, #23a6d5, #23d5ab);
        border-radius: 10px;
        padding-top: 1px;
        padding-bottom: 1px;
    }


</style>


<body>

<div class="da-head">
<h2> 
Our First Client ☎️
</h2>
</div>
<div class="midspan">
<h3> Client Side </h3>
<h4> Concept </h4>
<p>
So now that we have a Socket Server using we need to match the protocol and connect to the IP and Port addresses. Is successfully connected it means that the "3-way handshake" has been made and we can start sending data packets to the Server.
</p>
<h3> Imports </h3>
<p>
Same as with the Server we will need to import socket and threading.
</p>

<div class="segment">
<u style="background-color: #111111F7; margin-left: 10px;"> first_tcp_client.py</u>


<div class="code_it">
import socket<br>
import threading as thr<br>
from thr import Thread as Thr<br>
</div>

</div>
<br>

</div>
<br>

<br>
<br>
<br>
<br>
<br>
<br>
<div class="midspan">



<h3> The Connection </h3>
<p>
In order to make the FTP sockets behave in the 'seemlessly' continual manner which a client would expect it to; We will have to run 2 threads simultaneously:<br>
<span style="color: #00ff00; font-size: 15px;">Thread_1 => Send Data to Server</span><br>
<span style="color: #00ff00; font-size: 15px;">Thread_2 => Recv Data to Server</span>

</p>

<h3> The Point of OOP </h3>
<p>
Since we are no longer crawling, but walking with python, we want to have the <span style="color: #00ff00;"> main.py</span> and <span style="color: #00ff00;">conns.py</span> in two seperate files.
</p>
<h3> What <span style="color: #7a14ff;">return</span> ? </h3>
<p>
Since we will be using threading, there's no way to <span style="color: #7a14ff;">return</span> data. To work around this, we will need to mimic the lower level styles..<br>
We will write data to a file, and just keep reading it on every loop.
</p>
<br>
</div>


<br>
<br>
<br>

<br>
<br>
<br>
<div class="midspan">
<h3> File Management </h3>
<p>
The conventual way to go about this would be to use a library such as pandas. Be it that pandas is quite useful and has quite a few options, we will still be going vanilla for the duration of this series. So I have prepared my own <span style="color: #00ff00;"> File_Man.py</span> which I originally built for a simple project, and have found it to be quite useful.
<br>
I suppose it should go without saying that we will need to have the file in the project directory, and import it in both <span style="color: #00ff00;"> main.py</span> and <span style="color: #00ff00;">conns.py</span> files.
</p>

<div class="segment">
<u style="background-color: #111111F7; margin-left: 10px;"> main.py</u>
 &nbsp; &&<u style="background-color: #111111F7; margin-left: 10px;">conns.py</u>
<div class="code_it">
<span style="color: #7a14ff;">from</span> File_man <span style="color: #7a14ff;">import</span> File_Man
</div>
</div>

<br>
<p>
We will now be able to use the functions:<br>
<span style="color: yellow;">read_file</span><span style="color: cyan;">(file_name, delim)</span> 
<span style="color: yellow;">write_file</span><span style="color: cyan;">(file_name, data, delim)</span> 
<br>

<br>
</div>
<br>
<br>
<br>
<br>
<div class="midspan">


<h3> Connections<span style="font-size: xx-small;">dot</span>py</h3>


<p>
Now that we have the <span style="color: #00ff00;">conns.py</span>, we need to make the primary function, which will start the threads for <span style="color: yellow;">send_msg</span> and <span style="color: yellow;">recv_msg</span>.
</p>

<h3><span style="color: yellow;">start_conn</span></h3>
<p>
With this function with will give the parameters of <span style="color: cyan;">(set_ip, set_port)</span>.<br>
Because we are doing this on our local machine, we will be using:
</p>
<div class="segment">
<u style="background-color: #111111F7; margin-left: 10px;"> main.py</u>
<div class="code_it">
<span style="color: #01ff01;">ip_addr &nbsp; &nbsp;  = '127.0.0.1'</span><br/>
<span style="color: #01ff01;">port_num &nbsp;= 80</span>
</div>
</div>
<br>

<p>
In this funtion we need to configure socket, connect to target ip and start the 
<span style="color: yellow;">
send_msg()
</span> 
and 
<span style="color: yellow;">
recv_msg()
</span>
 threads.
<span style="color: yellow;">
recv_msg()
</span>
 will write any new data to a "
<span style="color: blue; font-size: small;">
IN_BOUND.txt
</span>
".
<span style="color: yellow; ">
send_msg()
</span> 
 will keep reading "
 <span style="color: blue; font-size: small;">
 OUT_BOUND.txt
 </span>
 " and send that data to the server, if there's any changes to the file.
</p>







</div>

<br>
<br>
<br>

<br>
<br>
<br>
<br>
<br>
<br>




<br>
<br>
<div class="midspan">
<h3> Client Side Socket </h3>

<h4> <u> Configuration </u> </h4>
<div class="segment">
<div class="code_it">
<span style="color: cyan; font-size: small;">
self
</span>.host =  set_ip<br>
<span style="color: cyan; font-size: small;">
self
</span>.port =  set_port<br>
<span style="color: cyan; font-size: small;">
self
</span>.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)<br>
</div>
</div>

<h4> <u>Connection </u> </h4>
<div class="segment">
<div class="code_it">
<span style="color: cyan; font-size: small;">
self
</span>.sock.connect((self.host, self.port))<br>
</div>
</div>



<h4> <u>Call Thread Function</u> </h4>
<div class="segment">
<div class="code_it">
<span style="color: cyan; font-size: small;">
self
</span>.con_threads()<br>
</div>
</div>
<br>

<h4> <u>Start Threads</u> </h4>

<div class="segment">
<div class="code_it">

<span style="color: blue; margin-left: -3px;">
def
</span> con_threads(self):<br>
&nbsp; <span style="color: cyan;">
self
</span>.recv = Thr(target=self.recv_msg)<br>
&nbsp; <span style="color: cyan;">
self
</span>.watch = Thr(target=self.send_msg)<br>
&nbsp; <span style="color: cyan;">
self
</span>.recv.start()<br>
&nbsp; <span style="color: cyan;">
self
</span>.watch.start()<br>

</div>
</div>
<br>
<br>
</div>
<br>
<br>
<br>
<br>

<br>
<br>

</div>
</div>

</div>



<br>
<br>
<br>
<br>
<div class="midspan">
<h3> Get Messages </h3>

<h4> The Loop </h4>
<p>Same as with the server, we will use threading <span style="color: #1814ff; font-size: medium;">Events</span>.</p>

<div class="segment">
<u style="background-color: #111111F7; margin-left: 10px;">get_msg()</u>
<div class="code_it">

<span style="color: cyan;  margin-right: 0px;">self</span>.E = thr.Event()<br>
<span style="color: #7a14f2;  margin-right: 3px;">
while</span>True:<br>
&nbsp; &nbsp; data = ""<br>

</div>
</div>

<h4> The Message </h4>

<div class="segment">
<u style="background-color: #111111F7; margin-left: 10px;">Wait until msg_len has been recieved</u>
<div class="code_it">

<div style=" display: block; margin-left: 0px; position: absolute;">data_len = int(<br>&nbsp; &nbsp; &nbsp; self.sock.recv(64).decode())</div>
<br>
<br>
if not data_len:<br>
&nbsp; &nbsp; 
<span style="color: cyan; margin-right: 0px;"> 
self
</span>.E.wait()<br>
if int(data_len) > 0:<br>
&nbsp; &nbsp; data = str(<br>
&nbsp; &nbsp; &nbsp; &nbsp; <span style="color: cyan;  margin-right: 0px;">self</span>.sock.recv(<br>
&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; data_len).decode())<br>

</div>
</div>
<br>
<p>
Now simply save that data to <span style="color: yellow; font-size: 13px;">OUT_BOUND.txt</span> for main to read it.
<br>
</div>
<br>
<br>
<br>
<br>
<br>
<br>






















<br>
<br>
<br>
<br>
<br>

<div class="midspan">




<h3> Send Message </h3>

<p>
So now that <span style="color: cyan;">get_msg()</span> has recieved the data at the exact length, we need to read that data in our main. From there, we can write a new message to the the <span style="color: yellow; font-size: 12px">OUT_BOUND.txt</span> and  <span style="color: cyan;">send_msg()</span> will read it and send it the the server.
</P>

<h4> How Do We Respond? </h4>

<!-- Simple Code Block  -->
<div class="segment">
<!-- With File_Name Header -->
<u style="background-color: #111111F7; margin-left: 10px;"> send_msg() -> in while loop</u>
<div class="code_it">


msg_len = len(toSend)<br>
send_len = str(msg_len).encode()<br>
send_len += b' ' * (64 - len(send_len))<br>
<span style="color: cyan;  margin-right: 0px;">self</span>.sock.send(send_len)<br>
<span style="color: cyan;  margin-right: 0px;">self</span>.sock.send(toSend.encode())<br>
#RESET DATA<br>
<span style="color: cyan;  margin-right: 0px;">self</span>.init_data = self.data<br>
toSend = ""<br>

</div>

</div>

<h4> Now What? </h4>

<p>
Next part, we start testing...
</p>

<br>



</div>

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>








<div class="tb_sh_0">
<div class="code_it">
msg_len = len(data)<br>
send_len = str(msg_len).encode()<br>
send_len += b' ' * (64 - len(send_len))<br>
conn.send(send_len)<br>
conn.send(data.encode())<br>
</div>
</div>


<br>

<h3>Next:</h3>
<p> We will build the client side code, and start communicating.
</p>








<!-- Simple Code Block  -->
<div class="segment">
<!-- With File_Name Header -->
<u style="background-color: #111111F7; margin-left: 10px;"> first_tcp_client.py</u>


<div class="code_it">
import socket<br>
import threading as thr<br>
from thr import Thread as Thr<br>
</div>

</div>
<br>



<!-- Some Colorful Stuff -->
<div class="tb_sh_0">
<div class="tb_box">
::::TESTING_VH:::::
</div>
</div>
<br>
</div>
<br>
<br>



<!-- No LineBreak Edit'n -->
<span style="color: blue; font-size: small;">
 OUT_BOUND.txt
 </span>

<!-- If you are crafty, you can make subliminal messages, lol -->
<p style="font-size: 9px">Make sure to check spelling of file & class names</p>







<br>
<br>
<br>
<br>
<br>

<div class="midspan" style="width: 95vw; height: 90vh;">
<br>
<br>

<div class="tb_sh_0">
<div class="tb_box">
<div style="margin-left: 45px">
<h2>SnrokL : Part 1-A-1</h2>
<h4>Client Side Connections</h4>
</div>

</div>
</div>
<br>
<br>
<br>
<br>
<div class="tb_sh_0">
<div style="position: relative; overflow-y: hidden; margin-top: -1px; ">
<p>
1 0 0 1 0 1 1 0 0 1 0 1 1 0 1 <br>
1 0 1 0 1 0 1 0 1 0 0 1 0 1 1 <br>
0 1 0 0 0 1 0 1 0 0 1 0 1 0 1 <br>
1 0 1 0 1 1 1 0 1 0 0 1 0 0 1 <br>
0 1 0 1 0 1 0 1 0 1 0 0 1 1 1 <br>
1 0 0 1 0 1 1 0 0 1 0 1 1 0 1 <br>
1 0 1 0 1 0 1 0 1 0 0 1 0 1 1 <br>
0 1 0 0 0 1 0 1 0 0 1 0 1 0 1 <br>
1 0 1 0 1 1 1 0 1 0 0 1 0 0 1 <br>
0 1 0 1 0 1 0 1 0 1 0 0 1 1 1 <br>
</p>
</div>
<div class="tb_box" 
style="
    position: absolute;  
    height: 240px;
    margin-top: -15.25em; 
    z-index: 2; 
    width: 65vw;
    margin-left: 2.5%;">

<div style="
    position: absolute;  
    margin-top: 8px; 
    margin-left: 30px;
    height: 240px;
    font-size: 10px; 
    position: relative;">
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠋⣠⣶⠆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⣰⡟⢁⠼⠛⢁⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⢠⡟⠀⣠⣴⠾⠟⠛⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡈⠀⠞⠀⠚⠉⢀⣤⡆⢰⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠻⣿⣶⣄⠐⠾⠀⣾⡿⠀⠈⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣷⣄⠙⢿⣷⠆⠀⠠⠤⠶⣤⣄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⠸⣿⣿⣿⣿⣿⣿⡆⠁⠀⠀⠀⠀⠀⠀⢹⡇
⠀⠀⠀⠀⠀⠀⠀⠰⢿⣷⣄⠙⢿⣿⣿⠏⠀⠀⠀⠀⠀⢀⣠⣴⠟⠁
⠀⢀⡀⠀⣾⡿⠀⡶⠄⠙⠿⣿⣦⠉⠁⠀⢀⣤⡴⠖⠛⠉⠉⠀⠀⠀
⠀⣾⠇⠸⠛⠁⣀⡤⠀⡴⠀⡈⠃⠀⠀⢰⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣤⣴⡶⠟⠋⠀⣼⠃⣸⡇⠀⠀⠀⠸⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⢁⣤⡖⢁⣼⠏⢰⣿⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠰⠿⠋⣠⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⢦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀
</div>



</div>
</div>
<br>
</div>
<br>
</div>

<br>
<br>
</body>