

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
        margin-right: -5%;
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
        margin-right: -5%;
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
    .midspan *{
        margin-left: 35px;
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

        width: 60vw;
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
        padding-bottom: 2%;

        width: 98%;
        height: calc(fit-content + 5px);
        background-color: black;
        border-radius: 14px;
        display: block;

    }
    .tb_box_1 *{
        font-size: small;
    }

    .tb_sh_1 {
        margin-left: 25px;
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
<h2 style="margin-left: 55px;"> 
Let's Connect 💻
</h2>
</div>
<div class="midspan">
<h3> Client Server Connection </h3>
<h4> Concept </h4>
<p>
<ul>
<li>
We will now test that the server is running
</li>
<li>
Start client side, connecting to server
</li>
<li>
Send server a message, and check the response
</li>
</ul>
</p>
<h4> Client's main </h4>
<p>
Let's import the File_Man and Connections file into our main, and run a while loop.
</p>

<div class="segment">
<u style="background-color: #111111F7; margin-left: 10px;"> main.py -> client-side</u>


<div class="code_it">
self.conn.start_conn("127.0.0.1", 8085)<br>
while True:<br>
 &nbsp; &nbsp;to_send = input("[MSG-to-SERVER]: ")+"*"<br>
 &nbsp; &nbsp;self.FM.write_file("OUT_BOUND.txt", to_send, "*", "w")<br>
 &nbsp; &nbsp;to_getn = self.FM.read_file("IN_BOUND.txt", "*")<br>
 &nbsp; &nbsp;for t in to_getn:<br>
 &nbsp; &nbsp; &nbsp; &nbsp;to_print += str(t)<br>
 &nbsp; &nbsp;print(f"[SERVER-RESPONSE]: {to_print}")<br>
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

<h3> Start The Server </h3>

<p> Now that we have both the server and the client side codes, let's run the server.</p>

<div class="tb_sh_1">
<div class="tb_box_1"  style="color: green;">

└─$ python3 server.py<br>
 &nbsp; &nbsp;[BINDING] <br>
 &nbsp; &nbsp;[LISTENING]
</div>
</div>

<h3> Start The Client </h3>

<div class="tb_sh_1">
<div class="tb_box_1"  style="color: green;">

└─$ python3 main.py
 &nbsp; &nbsp;[CONNECTED] <br>
 &nbsp; &nbsp;[GET_MSG]:[RUNNING] <br>
 &nbsp; &nbsp;[SEND_MSG]:[RUNNING] <br>
 &nbsp; &nbsp;[THREADS_RUNNING]:[RECV]:[SEND] <br>
</div>
</div>





<h3> Check the Server </h3>

<div class="tb_sh_1">
<div class="tb_box_1"  style="color: green;">

└─$ python3 server.py<br>
 &nbsp; &nbsp;[Client]:[CONNECTED]: ('127.0.0.1', 49852)<br>

</div>
</div>
<br>
<br>
</div>



<br>
<br>
<br>
<div class="midspan">

<h3> Greet The Server </h3>

<p> On the client side, send the "Hello Server!" message. </p>

<div class="tb_sh_1">
<div class="tb_box_1"  style="color: green;">

 &nbsp; &nbsp;[MSG-to-SERVER]: Hello Server! <br>


</div>
</div>

<h3> Check the server side </h3>
<p> The server side client_handle has now recieved the message and will respond accordingly
</p>
<div class="tb_sh_1">
<div class="tb_box_1"  style="color: green;">

 &nbsp; &nbsp;[CLIENT]->[SERVER]:: [Hello Server!] <br>
 &nbsp; &nbsp;[SERVER]->[CLIENT]:: [Hello Client!] <br>

</div>
</div>




<h3> Check the Response on the Client side </h3>
<p> If all has gone well, you should be seeing:

<div class="tb_sh_1">
<div class="tb_box_1"  style="color: green;">

 &nbsp; &nbsp;[SERVER-RESPONSE]: Hello Client! <br>

</div>
</div>
<br>
<br>
</div>




<br><br><br><br><br><br>



<div class="da-head">
<h2 style="margin-left: 55px;"> 
Conclusion
</h2>
</div>
<br>
<div class="midspan">

<h3> Intention </h3>

<p> We now have a base test model for which we can use to monitor data flow in an controlled environment.<br>
Meaning, we can easily analyze the flow of data, when we are already aware of the IP addresses involved, ports in use and the expected payload data.<br>
 </p>


<h4> Next up  </h4>
<p>
We will start building the 'listener_.py'.<br>
Where we use 'socket.recvfrom(65536)', our boss-port.<br>

</p>


<br>




<br>
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
<br>
<br>
<br>














<!-- Simple Code Block  -->
<div class="segment">
<!-- With File_Name Header -->
<u style="background-color: #111111F7; margin-left: 10px;"> first_tcp_client.py</u>
<!-- The Inner Block -->
<div class="code_it">
<!-- Lines of code.. -->
import socket<br>
import threading as thr<br>
from thr import Thread as Thr<br>
</div>
</div>
<br>



<!-- Some Colorful Stuff -->
<div class="tb_sh_0">
<!-- The BlackBoard -->
<div class="tb_box">
<!-- The content -->
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
<div style="margin-left: 25px">
<h2>SnrokL : Part 1-A-2</h2>
<h4>The Greetings </h4>
</div>

</div>
</div>
<br>
<br>
<br>
<br>
<div class="tb_sh_0">
<div style="position: relative; overflow-y: hidden; margin-top: -1px; margin-left: -20px;">
<p>
1 0 0 1 0 1 1 0 0 1 1 0 0 1 0 1 1 0 1 <br>
1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 1 <br>
0 1 0 0 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 <br>
1 0 1 0 1 1 1 0 1 1 1 0 1 0 0 1 0 0 1 <br>
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 1 1 <br>
1 0 0 1 0 1 1 0 0 1 1 0 0 1 0 1 1 0 1 <br>
1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 1 <br>
0 1 0 0 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 <br>
1 0 1 0 1 1 1 0 1 1 1 0 1 0 0 1 0 0 1 <br>
0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 1 1 <br>
</p>
</div>
<div class="tb_box" 
style="
    position: absolute;  
    height: 240px;
    margin-top: -15.25em; 
    z-index: 2; 
    width: 58%;
    margin-left: 1.9%;">

<div style="
    position: absolute;  
    margin-top: 8px; 
    margin-left: 30px;
    height: 240px;
    font-size: 10px; 
    position: relative;">



⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⢀⡀⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⣧⣄⢀⡀⣠⣼⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⣿⠀⠀⣿⣄⢀⡀⣠⣿⠀⠀⣿
⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏
⠀⠀⠀⠀⠀⠸⣧⣿⣿⣿⣿⣿⣿⣿⠏
</div>



</div>
</div>
<br>
</div>
<br>
</div>

<br>
<br>

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⢀⡀⣷
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⣧⣄⢀⡀⣠⣼⠀⠀⠀⣿⠀⠀⣿
⠀⠀⠀⠀⣿⠀⠀⣿⣄⢀⡀⣠⣿⠀⠀⣿
⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⣼⠏
⠀⠀⠀⠀⠀⠸⣧⣿⣿⣿⣿⣿⣿⣿⠏








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



</body>










