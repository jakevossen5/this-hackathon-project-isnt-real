from flask import Flask
app = Flask(__name__)

title = "Test title"
sub_title = "This is a subtitle"
insp = "This is some great inspiration"
what_it_does = "it does some cool things"
how_we_build = "we built it using some skills"
challenges = "lots oc challenges"
acomplishments = "wow we are so proud"
what_learned = "learned a lot of cool things"
whats_next = "this is whats next"


the_site = '''
<!DOCTYPE html>
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7 lte-ie9"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8 lte-ie9"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9 lte-ie9"> <![endif]-->
<!--[if IE 9]>         <html class="no-js lte-ie9"> <![endif]-->
<!--[if gt IE 9]><!--> <html lang="en" class="no-js" xmlns:fb="http://ogp.me/ns/fb#" xmlns:fb="http://www.facebook.com/2008/fbml" xmlns:og="http://opengraphprotocol.org/schema/" itemscope="itemscope" itemtype="http://schema.org/SoftwareApplication"> <!--<![endif]-->
  <head prefix="og: http://ogp.me/ns# fb: http://ogp.me/ns/fb# challengepost: http://ogp.me/ns/fb/challengepost#">
    <!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-WCFRZ3V');</script>
<!-- End Google Tag Manager -->


    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
<script type="text/javascript">window.NREUM||(NREUM={});NREUM.info={"beacon":"bam.nr-data.net","errorBeacon":"bam.nr-data.net","licenseKey":"f9082fa052","applicationID":"7341974","transactionName":"IQpdERFeXFVVRhpbCw8AHBYMV0ROUUZQQEsRDVwS","queueTime":1,"applicationTime":227,"agent":""}</script>
<script type="text/javascript">(window.NREUM||(NREUM={})).loader_config={licenseKey:"f9082fa052",applicationID:"7341974"};window.NREUM||(NREUM={}),__nr_require=function(e,n,t){function r(t){if(!n[t]){var o=n[t]={exports:{}};e[t][0].call(o.exports,function(n){var o=e[t][1][n];return r(o||n)},o,o.exports)}return n[t].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<t.length;o++)r(t[o]);return r}({1:[function(e,n,t){function r(){}function o(e,n,t){return function(){return i(e,[c.now()].concat(u(arguments)),n?null:this,t),n?void 0:this}}var i=e("handle"),a=e(3),u=e(4),f=e("ee").get("tracer"),c=e("loader"),s=NREUM;"undefined"==typeof window.newrelic&&(newrelic=s);var p=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],d="api-",l=d+"ixn-";a(p,function(e,n){s[n]=o(d+n,!0,"api")}),s.addPageAction=o(d+"addPageAction",!0),s.setCurrentRouteName=o(d+"routeName",!0),n.exports=newrelic,s.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(e,n){var t={},r=this,o="function"==typeof n;return i(l+"tracer",[c.now(),e,t],r),function(){if(f.emit((o?"":"no-")+"fn-start",[c.now(),r,o],t),o)try{return n.apply(this,arguments)}catch(e){throw f.emit("fn-err",[arguments,this,e],t),e}finally{f.emit("fn-end",[c.now()],t)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(e,n){m[n]=o(l+n)}),newrelic.noticeError=function(e,n){"string"==typeof e&&(e=new Error(e)),i("err",[e,c.now(),!1,n])}},{}],2:[function(e,n,t){function r(e,n){if(!o)return!1;if(e!==o)return!1;if(!n)return!0;if(!i)return!1;for(var t=i.split("."),r=n.split("."),a=0;a<r.length;a++)if(r[a]!==t[a])return!1;return!0}var o=null,i=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var u=navigator.userAgent,f=u.match(a);f&&u.indexOf("Chrome")===-1&&u.indexOf("Chromium")===-1&&(o="Safari",i=f[1])}n.exports={agent:o,version:i,match:r}},{}],3:[function(e,n,t){function r(e,n){var t=[],r="",i=0;for(r in e)o.call(e,r)&&(t[i]=n(r,e[r]),i+=1);return t}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],4:[function(e,n,t){function r(e,n,t){n||(n=0),"undefined"==typeof t&&(t=e?e.length:0);for(var r=-1,o=t-n||0,i=Array(o<0?0:o);++r<o;)i[r]=e[n+r];return i}n.exports=r},{}],5:[function(e,n,t){n.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(e,n,t){function r(){}function o(e){function n(e){return e&&e instanceof r?e:e?f(e,u,i):i()}function t(t,r,o,i){if(!d.aborted||i){e&&e(t,r,o);for(var a=n(o),u=v(t),f=u.length,c=0;c<f;c++)u[c].apply(a,r);var p=s[y[t]];return p&&p.push([b,t,r,a]),a}}function l(e,n){h[e]=v(e).concat(n)}function m(e,n){var t=h[e];if(t)for(var r=0;r<t.length;r++)t[r]===n&&t.splice(r,1)}function v(e){return h[e]||[]}function g(e){return p[e]=p[e]||o(t)}function w(e,n){c(e,function(e,t){n=n||"feature",y[t]=n,n in s||(s[n]=[])})}var h={},y={},b={on:l,addEventListener:l,removeEventListener:m,emit:t,get:g,listeners:v,context:n,buffer:w,abort:a,aborted:!1};return b}function i(){return new r}function a(){(s.api||s.feature)&&(d.aborted=!0,s=d.backlog={})}var u="nr@context",f=e("gos"),c=e(3),s={},p={},d=n.exports=o();d.backlog=s},{}],gos:[function(e,n,t){function r(e,n,t){if(o.call(e,n))return e[n];var r=t();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(e,n,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return e[n]=r,r}var o=Object.prototype.hasOwnProperty;n.exports=r},{}],handle:[function(e,n,t){function r(e,n,t,r){o.buffer([e],r),o.emit(e,n,t)}var o=e("ee").get("handle");n.exports=r,r.ee=o},{}],id:[function(e,n,t){function r(e){var n=typeof e;return!e||"object"!==n&&"function"!==n?-1:e===window?0:a(e,i,function(){return o++})}var o=1,i="nr@id",a=e("gos");n.exports=r},{}],loader:[function(e,n,t){function r(){if(!E++){var e=x.info=NREUM.info,n=l.getElementsByTagName("script")[0];if(setTimeout(s.abort,3e4),!(e&&e.licenseKey&&e.applicationID&&n))return s.abort();c(y,function(n,t){e[n]||(e[n]=t)}),f("mark",["onload",a()+x.offset],null,"api");var t=l.createElement("script");t.src="https://"+e.agent,n.parentNode.insertBefore(t,n)}}function o(){"complete"===l.readyState&&i()}function i(){f("mark",["domContent",a()+x.offset],null,"api")}function a(){return O.exists&&performance.now?Math.round(performance.now()):(u=Math.max((new Date).getTime(),u))-x.offset}var u=(new Date).getTime(),f=e("handle"),c=e(3),s=e("ee"),p=e(2),d=window,l=d.document,m="addEventListener",v="attachEvent",g=d.XMLHttpRequest,w=g&&g.prototype;NREUM.o={ST:setTimeout,SI:d.setImmediate,CT:clearTimeout,XHR:g,REQ:d.Request,EV:d.Event,PR:d.Promise,MO:d.MutationObserver};var h=""+location,y={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-1130.min.js"},b=g&&w&&w[m]&&!/CriOS/.test(navigator.userAgent),x=n.exports={offset:u,now:a,origin:h,features:{},xhrWrappable:b,userAgent:p};e(1),l[m]?(l[m]("DOMContentLoaded",i,!1),d[m]("load",r,!1)):(l[v]("onreadystatechange",o),d[v]("onload",r)),f("mark",["firstbyte",u],null,"api");var E=0,O=e(5)},{}]},{},["loader"]);</script>
    <meta name="viewport" content="width=device-width">
    <title>Cookie Injection but with Real Cookies | Devpost</title>

    <meta name="description" content="Cookie Injection but with Real Cookies - What if we used a Cookie Monster and a cookie to represent HTTP request to teach cybersecurity to kids?" />
<meta property="fb:app_id" content="115745995110194" />
<meta property="og:title" content="Cookie Injection but with Real Cookies" />
<meta property="og:description" content="What if we used a Cookie Monster and a cookie to represent HTTP request to teach cybersecurity to kids?" />
<meta property="og:type" content="challengepost:app" />
<meta property="og:site_name" content="Devpost" />
<meta property="og:image" content="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_thumbnail_photos/000/770/184/datas/medium.png" />
<meta property="og:url" content="http://devpost.com/software/cookie-injection-but-with-real-cookies" />
<meta name="twitter:card" content="summary" />
<meta name="twitter:site" content="@Devpost" />
<meta name="twitter:title" content="Cookie Injection but with Real Cookies" />
<meta name="twitter:description" content="What if we used a Cookie Monster and a cookie to represent HTTP request to teach cybersecurity to kids?" />
<meta name="twitter:image" content="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_thumbnail_photos/000/770/184/datas/medium.png" />
<meta name="twitter:domain" content="devpost.com" />
<meta name="twitter:url" content="http://devpost.com/software/cookie-injection-but-with-real-cookies" />
<meta itemprop="name" content="Cookie Injection but with Real Cookies" />
<meta itemprop="description" content="What if we used a Cookie Monster and a cookie to represent HTTP request to teach cybersecurity to kids?" />
<meta itemprop="image" content="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_thumbnail_photos/000/770/184/datas/medium.png" />
<meta itemprop="screenshot" content="https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_thumbnail_photos/000/770/184/datas/medium.png" />
    <meta name="csrf-param" content="authenticity_token" />
<meta name="csrf-token" content="UEuAM8s5O7ZU0XT4H4ZKl93Xe4sTvkdy9GmbntLWEJ8O9/YhsraSMi9f0uh/LqwIQOCqdwfC1FD3hbYaWJPPtw==" />


    <!--[if gt IE 7]><!-->
    <link rel="stylesheet" media="screen" href="https://use.fontawesome.com/releases/v5.8.1/css/all.css" integrity="sha384-50oBUHEmvpQ+1lW4y57PTFmhCaXp0ML5d60M1M7uH2+nqUivzIebhndOJK28anvf" crossorigin="anonymous" />
    <link rel="stylesheet" media="screen" href="https://devpost-challengepost.netdna-ssl.com/assets/reimagine2-48924748bc4255e58c6e2d8dc62e5a07.css" />
    <link rel="stylesheet" media="screen" href="https://devpost-challengepost.netdna-ssl.com/assets/home/home_application-8987b2180219f1e4863006d6c3246c0f.css" />

    <script src="https://devpost-challengepost.netdna-ssl.com/assets/modernizr-bef57869320b416d48fb2c5087d5e793.js"></script>
    <!--<![endif]-->

    <link href="https://plus.google.com/100989403125217127946" rel="publisher">
  </head>

  <body id="body-softwares" class="foundation-grid action-show controller-softwares engine-home">
    <!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-WCFRZ3V"
                  height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->



    <!--googleoff: anchor-->

<!--[if lte IE 9 ]>
  <div id="unsupported_browser_version" class="persistent_message alert-box alert">
    <p>
      We've detected that you are using an unsupported browser.  Please
      <a href="http://browsehappy.com/">upgrade your browser</a>
      to Internet Explorer 10 or higher.
    </p>
  </div>
<![endif]-->


<!--googleon: anchor-->




    <div class="alert-box newsletter-alert" data-newsletter-alert="base">
  <div class="row">
    <div class="small-12 columns">
      <div class="clearfix">
        <img alt="✉" class="left newsletter-alert-icon" src="https://devpost-challengepost.netdna-ssl.com/assets/shared/newsletter-promo-banner-email-e8dbc554d75cdf189b3574ae5f918949.png" />

        <div class="left newsletter-alert-message">
          <h4>You're missing out!</h4>

          <p>
            Sign up for our weekly newsletter to learn about hackathons, community updates, and awesome projects.
          </p>
        </div>

        <p class="left">
          <a class="button radius newsletter-alert-cta-button" rel="nofollow" data-method="post" href="/newsletters/subscribe?flow%5Bname%5D=subscribe_to_newsletter">Sign me up</a>
        </p>

        <a href="#" class="close" data-newsletter-alert="close">&times;</a>
      </div>
    </div>
  </div>
</div>







<header id="global-nav">
  <div class="contain-to-grid hide-for-large-up">
  <nav class="top-bar" data-topbar>
    <ul class="title-area top-bar-section">
      <li>
        <a class="toggle-topbar has-dropdown text-center" data-target-menu="world" id="hamburger" href="#">
          <i class="ss-icon ss-rows"></i>
</a>      </li>
      <li class="name">

        <span id="logo">
  <a href="https://devpost.com">
    <img alt="Devpost" src="https://devpost-challengepost.netdna-ssl.com/assets/reimagine2/devpost-logo-646bdf6ac6663230947a952f8d354cad.svg" />
</a></span>

      </li>

        <li class="toggle-topbar has-dropdown" data-target-menu="user">
    <a class="user" id="global-nav-screen-name" aria-label="Access your account menu" href="https://devpost.com/jakevossen?ref_content=user-portfolio&amp;ref_feature=portfolio&amp;ref_medium=global-nav">
      <img alt="jakevossen" class="user-avatar user-photo gravatar_image image-replacement" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="https://www.gravatar.com/avatar/b6cfd75473ae34088eaad669c442988e?d=https%3A%2F%2Fdevpost-challengepost.netdna-ssl.com%2Fassets%2Fdefaults%2Fno-avatar-25.png&amp;s=25" />

</a>  </li>


    </ul>

    <section class="top-bar-section" data-top-nav-menu="user">
        <ul class="right logged-in">
  <li class="divider"></li>
  <li>
    <a href="https://devpost.com/jakevossen?ref_content=user-portfolio&amp;ref_feature=portfolio&amp;ref_medium=global-nav">Portfolio</a>
  </li>
  <li class="divider"></li>



  <li id="global-nav-user-settings">
    <a href="https://devpost.com/settings">Settings</a>
  </li>
  <li class="divider"></li>

  <li id="global-nav-user-log-out" data-global-nav-user="log-out">
    <a href="https://secure.devpost.com/users/logout">Log out</a>
  </li>
  <li class="divider"></li>


</ul>


    </section>

    <section class="top-bar-section" data-top-nav-menu="world">
      <ul class="right">
  <li class="divider"></li>
<li>
  <a class="main-link" data-role="discover" href="https://devpost.com/hackathons">
    Hackathons
</a></li>
<li class="divider"></li>
<li>
  <a class="main-link" data-role="projects" href="https://devpost.com/software">
    Projects
</a></li>
<li class="divider"></li>
<li>
  <a class="main-link" data-role="for-orgs" href="https://post.devpost.com">
    For organizations
</a></li>

</ul>

    </section>
  </nav>
</div>

  <div class="contain-to-grid hide-for-small hide-for-medium">
  <nav class="top-bar" data-topbar>
    <ul class="title-area">
      <li class="name">
        <span id="logo">
  <a href="https://devpost.com">
    <img alt="Devpost" src="https://devpost-challengepost.netdna-ssl.com/assets/reimagine2/devpost-logo-646bdf6ac6663230947a952f8d354cad.svg" />
</a></span>

      </li>
    </ul>

    <section class="top-bar-section">
      <ul class="left">
  <li class="divider"></li>
<li>
  <a class="main-link" data-role="discover" href="https://devpost.com/hackathons">
    Hackathons
</a></li>
<li class="divider"></li>
<li>
  <a class="main-link" data-role="projects" href="https://devpost.com/software">
    Projects
</a></li>
<li class="divider"></li>
<li>
  <a class="main-link" data-role="for-orgs" href="https://post.devpost.com">
    For organizations
</a></li>

</ul>

        <ul class="right logged-in">
  <li class="hide-for-small" data-region="notification-bell">
  <a data-notification="bell" data-dropdown="notification-dd" id="notification-button" href="https://devpost.com/notifications"></a>
</li>


  <li class="has-dropdown" id="global-nav-user-dropdown">
    <a class="user" id="global-nav-screen-name" aria-label="Access your account menu" href="https://devpost.com/jakevossen?ref_content=user-portfolio&amp;ref_feature=portfolio&amp;ref_medium=global-nav">
      <img alt="jakevossen" class="user-avatar user-photo gravatar_image image-replacement" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="https://www.gravatar.com/avatar/b6cfd75473ae34088eaad669c442988e?d=https%3A%2F%2Fdevpost-challengepost.netdna-ssl.com%2Fassets%2Fdefaults%2Fno-avatar-32.png&amp;s=32" />

</a>
    <ul class="dropdown">
      <li class="divider"></li>

      <li>
        <a href="https://devpost.com/jakevossen?ref_content=user-portfolio&amp;ref_feature=portfolio&amp;ref_medium=global-nav">Portfolio</a>
      </li>
      <li class="divider"></li>



      <li id="global-nav-user-settings">
        <a href="https://devpost.com/settings">Settings</a>
      </li>
      <li class="divider"></li>

      <li id="global-nav-user-log-out" data-global-nav-user="log-out">
        <a href="https://secure.devpost.com/users/logout">Log out</a>
      </li>
      <li class="divider"></li>



    </ul>
  </li>
</ul>


    </section>
  </nav>
</div>

</header>


    <div id="notification-dd"
     class="f-dropdown medium"
     data-dropdown-content
     data-notification="dropdown">
  <header>
    <h6 class="text-center">Notifications</h6>
  </header>
  <div data-region="dropdown-feed">
    <p class="text-center loading">Loading...</p>
  </div>
  <footer class="text-center" data-region="footer">
  </footer>
</div>




    <section id="container">
        <header class="page-header text-center" id="software-header">

  <div class="row">
    <div class="small-12 columns">

        <h1 id="app-title">''' + title + '''</h1>

          <p class="large">''' + sub_title +  '''</p>

    </div>
  </div>

  <div class="row">
    <div class="small-12 columns">
      <div class="software-likes">
  <div data-like="base">
      <a class="like-button button radius secondary" data-like="like-button" rel="nofollow" data-method="post" href="/software/cookie-injection-but-with-real-cookies/likes">
  <span class="ss-icon ss-heart"></span>
  Like
</a>
</div>

</div>

      <a id="software-comment-button" class="button radius comment-button" href="/software/cookie-injection-but-with-real-cookies#updates">
  <span class="ss-icon ss-quote"></span>
  Comment
    <span class="side-count">3</span>
</a>

    </div>
  </div>
</header>


<nav id="software-nav">
  <div class="row">
    <div class="large-12 columns">
      <ul class="left no-bullet">
        <li>
          <h4>
            <a class="active" href="/software/cookie-injection-but-with-real-cookies">Story</a>
          </h4>
        </li>
        <li>
          <h4>
            <a href="/software/cookie-injection-but-with-real-cookies#updates">Updates <span class='side-count'>2</span></a>
          </h4>
        </li>
      </ul>
    </div>
  </div>
</nav>






<article id="app-details" class="content-section">
  <div class="row">
    <div class="large-9 columns" id="app-details-left">

    <div id="gallery">
      <ul data-orbit="true" data-options="animation_speed:0;slide_number:false;timer:false" class="no-bullet">

          <li class="text-center">
    <img alt="Cookie Injection but with Real Cookies – screenshot 1" class="software_photo_image image-replacement" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/thumbnail-placeholder-42bcab8d8178b413922ae2877d8b0868.gif&#39;;" src="//challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/770/181/datas/gallery.jpg" />
    <p>
      <i></i>
    </p>
</li>  <li class="text-center">
    <img alt="Cookie Injection but with Real Cookies – screenshot 2" class="software_photo_image image-replacement" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/thumbnail-placeholder-42bcab8d8178b413922ae2877d8b0868.gif&#39;;" src="//challengepost-s3-challengepost.netdna-ssl.com/photos/production/software_photos/000/770/183/datas/gallery.jpg" />
    <p>
      <i></i>
    </p>
</li>
</ul>    </div>



      <div>
  <h2>Inspiration</h2>

<p>''' + insp + '''</p>

<h2>What it does</h2>

<p>''' + what_it_does + '''</p>

<h2>How we built it</h2>

<p>''' + how_we_build + '''</p>

<h2>Challenges we ran into</h2>

<p>''' + challenges + '''</p>

<h2>Accomplishments that we're proud of</h2>

<p>''' + acomplishments + ''' </p>

<h2>What we learned</h2>

<p>''' + what_learned + '''</p>

<h2>What's next for ''' + title + '''</h2>

<p>''' + whats_next + '''</p>

</div>

        <div id="built-with" class="">
    <h2>Built With</h2>

    <ul class="no-bullet inline-list"><li><span class="cp-tag">godot</span></li></ul>
  </div>


    </div>

    <aside class="large-3 columns" id="app-details-right">
        <div class="section">
          <a class="button radius expand" href="/software/cookie-injection-but-with-real-cookies/edit">Edit project</a>
        </div>

        <div id="submissions" class="section">
    <h4 class="clearfix">
      Submitted to
    </h4>

    <ul class="software-list-with-thumbnail">
        <li>
    <figure class="software-list-thumbnail challenge_avatar">
      <a href="https://hackcuv.devpost.com/"><img alt="image" class="thumbnail_image image-replacement" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="//challengepost-s3-challengepost.netdna-ssl.com/photos/production/challenge_thumbnails/000/742/297/datas/medium.png" /></a>
    </figure>

    <div class="software-list-content">
      <p>
        <a href="https://hackcuv.devpost.com/">HackCU Episode V</a>
      </p>

          <ul class="no-bullet">
              <li>
                <span class="winner label radius small all-caps">Winner</span>
                Most RANDOM hack
              </li>
          </ul>

    </div>


  </li>

    </ul>
  </div>

      <section id="app-team">
  <h4 class="clearfix">
    Created by
  </h4>

  <ul class="no-bullet">

<li class="software-team-member" itemprop="member">
    <div class="bubble">
    <div data-contribution="editable-contribution">

      <div class="contribution">

        <div data-contribution="contribution">
            <p>Learned a ton about game design and co wrote the Whitepaper.</p>
        </div>

        <a class="" data-contribution="edit" href="/software/cookie-injection-but-with-real-cookies/members/414459/edit">edit</a>

      </div>

      <form class="simple_form hide" id="contribution-form" data-contribution="form" novalidate="novalidate" action="/software/cookie-injection-but-with-real-cookies/members/414459" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="_method" value="patch" /><input type="hidden" name="authenticity_token" value="Bzi9WIJoi6WYz/aQRw5GrBFb42KfjXwMT18+d2Y6IRRZhMtK++ciIeNBUIAnpqAzjGwynovx7y5MsxPz7H/+PA==" />
  <div class="input text optional software_member_contribution"><label class="text optional control-label" for="software_member_contribution">Describe your contribution</label><textarea class="text optional" placeholder="Ex: I worked on the back-end. It was my first time using Node, which was a little intimidating, but I learned a lot." name="software_member[contribution]" id="software_member_contribution">
Learned a ton about game design and co wrote the Whitepaper.</textarea></div>
  <input type="submit" name="commit" value="Save" class="button primary radius small" />
  <small>
    <a class="button-size" data-contribution="cancel" href="/software/cookie-injection-but-with-real-cookies">Cancel</a>
  </small>
</form>
    </div>
  </div>

  <div class="row">
    <div class="small-2 large-4 columns">
      <figure>
        <a class="user-profile-link" href="https://devpost.com/jakevossen"><img alt="Jacob Vossen" class="software-member-photo user-photo gravatar_image image-replacement" title="Jacob Vossen" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="https://www.gravatar.com/avatar/b6cfd75473ae34088eaad669c442988e?d=https%3A%2F%2Fdevpost-challengepost.netdna-ssl.com%2Fassets%2Fdefaults%2Fno-avatar-180.png&amp;s=180" /></a>
      </figure>
    </div>

    <div class="small-10 large-8 columns">
      <a class="user-profile-link" href="https://devpost.com/jakevossen">Jacob Vossen</a>
      <span class="follow-button-wrapper" data-context="software-detail" data-layout="condensed" data-follow-through-id="414459"></span>

        <br>
        <small></small>
    </div>
  </div>
</li>

<li class="software-team-member" itemprop="member">

  <div class="row">
    <div class="small-2 large-4 columns">
      <figure>
        <a class="user-profile-link" href="https://devpost.com/fisherdarling"><img alt="Fisher Darling" class="software-member-photo user-photo facebook_avatar_image image-replacement" title="Fisher Darling" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="https://avatars1.githubusercontent.com/u/14206675?v=4?height=180&amp;width=180" /></a>
      </figure>
    </div>

    <div class="small-10 large-8 columns">
      <a class="user-profile-link" href="https://devpost.com/fisherdarling">Fisher Darling</a>
      <span class="follow-button-wrapper" data-context="software-detail" data-layout="condensed" data-follow-through-id="414460"></span>

        <br>
        <small></small>
    </div>
  </div>
</li>

  </ul>

    <p class="software-add-team-members">
      <a href="/software/cookie-injection-but-with-real-cookies/edit#members">+ add team members</a>
    </p>
</section>


        <div class="section">
    <a id="flag" href="/software/cookie-injection-but-with-real-cookies/flags/new">
      <span class="ss-icon ss-flag small"></span>
      <small>Report inappropriate content</small>
</a>  </div>

        <div id="hide-delete">
    <a class="grey" rel="nofollow" data-method="put" href="https://devpost.com/software/cookie-injection-but-with-real-cookies/members/414459/toggle_visibility">
      <span class="ss-icon ss-view small"></span>
      <small>Hide project from my portfolio</small>
</a>
  </div>

    </aside>
  </div>
</article>

<section id="share-and-like">
  <div class="row">
    <div class="small-12 columns">
      <div class="clearfix">
        <div class="left">
          <div class="software-likes">
  <div data-like="base">
      <a class="like-button button radius secondary" data-like="like-button" rel="nofollow" data-method="post" href="/software/cookie-injection-but-with-real-cookies/likes">
  <span class="ss-icon ss-heart"></span>
  Like
</a>
</div>


  <span class="like-counts">

  </span>

  <ul class="like-users inline-list">
  </ul>

</div>

        </div>
        <div class="right hide-for-small">

<div id="software-share" class="hide" data-add-this-buttons="true">
  Share this project:



  <ul class="h-nav clearfix inline-list" id="social-links">
    <li id="promote-twitter">

<div class="social-icon">
  <div class="addthis_toolbox addthis_default_style addthis_32x32_style"
    addthis:url="http://devpost.com/software/cookie-injection-but-with-real-cookies?utm_campaign=portfolio-share&amp;utm_medium=twitter&amp;utm_source=cp"
    addthis:title="Check out Cookie Injection but with Real Cookies"
    addthis:description="http://devpost.com/software/cookie-injection-but-with-real-cookies">
    <a class="addthis_button_twitter"
      tw:count="false"
      tw:counturl="http://devpost.com/software/cookie-injection-but-with-real-cookies"
      tw:url="http://devpost.com/software/cookie-injection-but-with-real-cookies?utm_campaign=portfolio-share&amp;utm_medium=twitter&amp;utm_source=cp"
      tw:via="Devpost"
      tw:text="Check out Cookie Injection but with Real Cookies">
    </a>
  </div>
</div>

    </li>

    <li id="promote-fb-li">

<div class="social-icon">
  <div class="addthis_32x32_style addthis_toolbox addthis_default_style"
    addthis:url="http://devpost.com/software/cookie-injection-but-with-real-cookies"
    addthis:title="Cookie Injection but with Real Cookies"
    addthis:description="">
    <div class="custom_images">
      <a class="addthis_button_facebook"
        fb:like:show_faces="false">
      </a>
    </div>
  </div>
</div>

    </li>

    <li id="promote-reddit-li">
      <div class="social-icon">
  <a class="addthis_button_reddit addthis_32x32_style"
    addthis:url="http://devpost.com/software/cookie-injection-but-with-real-cookies?utm_campaign=portfolio-share&amp;utm_medium=reddit&amp;utm_source=cp"
    addthis:title="Cookie Injection but with Real Cookies"
    ></a>
</div>

    </li>
</ul>
</div>

        </div>
      </div>
    </div>
  </div>
</section>

<div id="hackathon-picker" class="reveal-modal small" data-reveal data-hackathon-picker>
  <a class="close-reveal-modal close-reveal-modal-x">&#215;</a>
  <div data-region="hackathon-picker-content"></div>
</div>



<article class="content-section">
  <div class="row">
    <div class="large-12 columns software-updates">
      <h2 id="updates">Updates</h2>
        <div class="content-section software-update-layout with-sidebar">
  <div class="row">
    <div class="large-8 small-12 columns">
      <div class="media">
        <div class="media-left">
          <a class="user-profile-link" href="https://devpost.com/jakevossen"><img alt="Jacob Vossen" class="user-avatar hide-for-small user-photo gravatar_image image-replacement" title="Jacob Vossen" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="https://www.gravatar.com/avatar/b6cfd75473ae34088eaad669c442988e?d=https%3A%2F%2Fdevpost-challengepost.netdna-ssl.com%2Fassets%2Fdefaults%2Fno-avatar-180.png&amp;s=180" /></a>
        </div>
        <div class="media-content">
          <form novalidate="novalidate" class="simple_form new_software_update" id="new_software_update" data-role="update-form" action="https://devpost.com/software/cookie-injection-but-with-real-cookies/updates#updates" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="3cFmiKC9eAUVEtVqs1DfUDbvEED8hLPxNzBSG/pGrt6DfRCa2TLRgW6cc3rT+DnPq9jBvOj4INM03H+fcANx9g==" />
            <div class="input text optional software_update_body field_with_hint"><label class="text optional control-label" for="software_update_body">Post an update about Cookie Injection but with Real Cookies</label><p class="hint">Keep a log of how Cookie Injection but with Real Cookies has evolved. Post about new features, app store releases, screenshots, or even code snippets. Your followers will see your updates in their feeds and can comment on them.</p><textarea class="text optional" placeholder="Use markdown for formatting." name="software_update[body]" id="software_update_body">
</textarea></div>

            <input type="hidden" name="location" id="location" value="project details page" />

            <input type="submit" name="commit" value="Post update" class="btn button radius" />
</form>        </div>
      </div>
    </div>
    <div class="columns"></div>
  </div>

</div>


      <article class="content-section software-update with-sidebar" data-commentable-id="166797">
  <div class="row">
    <div class="large-8 small-12 columns">
      <div data-region="actions"></div>

      <div class="media">
        <div class="media-left">
          <a class="update-user-avatar user-profile-link" href="https://devpost.com/jakevossen"><img alt="Jacob Vossen" class="user-avatar user-photo gravatar_image image-replacement" title="Jacob Vossen" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="https://www.gravatar.com/avatar/b6cfd75473ae34088eaad669c442988e?d=https%3A%2F%2Fdevpost-challengepost.netdna-ssl.com%2Fassets%2Fdefaults%2Fno-avatar-180.png&amp;s=180" /></a>
        </div>
        <div class="media-content">
          <p class="author small">
            <a class="user-profile-link" href="https://devpost.com/jakevossen">Jacob Vossen</a>
            posted an update
            <span class="light-text">
              &mdash;
              <a class="timestamp light-text" href="/software/cookie-injection-but-with-real-cookies/updates/166797">
                <time class="timeago" datetime="2019-02-26T12:13:20-05:00">
                  Feb 26, 2019 12:13 PM EST
                </time>
</a>            </span>
          </p>

          <p>Made open source MIT license, put GitHub link</p>


          <section class="software-update-comments" data-layout="comments">
  <div data-region="load-more"></div>
  <div data-region="comments"></div>

    <form class="simple_form comment-form" data-single-submit="true" novalidate="novalidate" id="new_comment" action="/software_updates/166797/comments" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="0flClWKc0RSBOKoXO3zVBac57DTs6iJ/QK2NY++2jIOPRTSHGxN4kPq2DAdb1DOaOg49yPiWsV1DQaDnZfNTqw==" />
    <h3>
      <label for="comment_body">Comments</label>
    </h3>

    <div class="comment-column">
      <div class="media">
        <div class="media-left">
          <a class="user-profile-link" href="https://devpost.com/jakevossen"><img alt="Jacob Vossen" class="user-avatar user-photo gravatar_image image-replacement" title="Jacob Vossen" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="https://www.gravatar.com/avatar/b6cfd75473ae34088eaad669c442988e?d=https%3A%2F%2Fdevpost-challengepost.netdna-ssl.com%2Fassets%2Fdefaults%2Fno-avatar-180.png&amp;s=180" /></a>
        </div>
        <div class="media-content">
          <div class="input text required comment_body"><textarea class="text required" placeholder="Write a comment" name="comment[body]" id="comment_body">
</textarea></div>
          <input type="hidden" name="comment[location]" id="comment_location" value="project detail page" />
          <input type="submit" name="commit" value="Post comment" class="btn button radius small" />
        </div>
      </div>
    </div>
</form>
</section>

        </div>
      </div>

    </div>
    <div class="columns"></div>
  </div>
</article>
<article class="content-section software-update with-sidebar" data-commentable-id="166661">
  <div class="row">
    <div class="large-8 small-12 columns">
      <div data-region="actions"></div>

      <div class="media">
        <div class="media-left">
          <a class="update-user-avatar user-profile-link" href="https://devpost.com/jakevossen"><img alt="Jacob Vossen" class="user-avatar user-photo gravatar_image image-replacement" title="Jacob Vossen" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="https://www.gravatar.com/avatar/b6cfd75473ae34088eaad669c442988e?d=https%3A%2F%2Fdevpost-challengepost.netdna-ssl.com%2Fassets%2Fdefaults%2Fno-avatar-180.png&amp;s=180" /></a>
        </div>
        <div class="media-content">
          <p class="author small">
            <a class="user-profile-link" href="https://devpost.com/jakevossen">Jacob Vossen</a>
            posted an update
            <span class="light-text">
              &mdash;
              <a class="timestamp light-text" href="/software/cookie-injection-but-with-real-cookies/updates/166661">
                <time class="timeago" datetime="2019-02-24T14:47:51-05:00">
                  Feb 24, 2019 02:47 PM EST
                </time>
</a>            </span>
          </p>

          <p>We are table 21 if you can't find us</p>


          <section class="software-update-comments" data-layout="comments">
  <div data-region="load-more"></div>
  <div data-region="comments"></div>

    <form class="simple_form comment-form" data-single-submit="true" novalidate="novalidate" id="new_comment" action="/software_updates/166661/comments" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="wQjalm+ZFsk3eXfOGFlZjG6nf/SGxQppIzzLnZKzLlaftKyEFha/TUz30d548b8T85CuCJK5mUsg0OYZGPbxfg==" />
    <h3>
      <label for="comment_body">Comments</label>
    </h3>

    <div class="comment-column">
      <div class="media">
        <div class="media-left">
          <a class="user-profile-link" href="https://devpost.com/jakevossen"><img alt="Jacob Vossen" class="user-avatar user-photo gravatar_image image-replacement" title="Jacob Vossen" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="https://www.gravatar.com/avatar/b6cfd75473ae34088eaad669c442988e?d=https%3A%2F%2Fdevpost-challengepost.netdna-ssl.com%2Fassets%2Fdefaults%2Fno-avatar-180.png&amp;s=180" /></a>
        </div>
        <div class="media-content">
          <div class="input text required comment_body"><textarea class="text required" placeholder="Write a comment" name="comment[body]" id="comment_body">
</textarea></div>
          <input type="hidden" name="comment[location]" id="comment_location" value="project detail page" />
          <input type="submit" name="commit" value="Post comment" class="btn button radius small" />
        </div>
      </div>
    </div>
</form>
</section>

        </div>
      </div>

    </div>
    <div class="columns"></div>
  </div>
</article>
<article class="content-section software-update with-sidebar" data-commentable-id="166243">
  <div class="row">
    <div class="large-8 small-12 columns">
      <div data-region="actions"></div>

      <div class="media">
        <div class="media-left">
          <a class="update-user-avatar user-profile-link" href="https://devpost.com/jakevossen"><img alt="Jacob Vossen" class="user-avatar user-photo gravatar_image image-replacement" title="Jacob Vossen" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="https://www.gravatar.com/avatar/b6cfd75473ae34088eaad669c442988e?d=https%3A%2F%2Fdevpost-challengepost.netdna-ssl.com%2Fassets%2Fdefaults%2Fno-avatar-180.png&amp;s=180" /></a>
        </div>
        <div class="media-content">
          <p class="author small">
            <a class="user-profile-link" href="https://devpost.com/jakevossen">Jacob Vossen</a>
            started this project
            <span class="light-text">
              &mdash;
              <a class="timestamp light-text" href="/software/cookie-injection-but-with-real-cookies/updates/166243">
                <time class="timeago" datetime="2019-02-24T08:45:24-05:00">
                  Feb 24, 2019 08:45 AM EST
                </time>
</a>            </span>
          </p>

          <p><i>Leave feedback in the comments!</i></p>

          <section class="software-update-comments" data-layout="comments">
  <div data-region="load-more"></div>
  <div data-region="comments"></div>

    <form class="simple_form comment-form" data-single-submit="true" novalidate="novalidate" id="new_comment" action="/software_updates/166243/comments" accept-charset="UTF-8" method="post"><input name="utf8" type="hidden" value="&#x2713;" /><input type="hidden" name="authenticity_token" value="0sFM7vlhJIFmWgLpb8lWGyxQ0ucsRTNCWJh3JBpyKe2MfTr8gO6NBR3UpPkPYbCEsWcDGzg5oGBbdFqgkDf2xQ==" />
    <h3>
      <label for="comment_body">Comments</label>
    </h3>

    <div class="comment-column">
      <div class="media">
        <div class="media-left">
          <a class="user-profile-link" href="https://devpost.com/jakevossen"><img alt="Jacob Vossen" class="user-avatar user-photo gravatar_image image-replacement" title="Jacob Vossen" onerror="this.onerror=null;this.src=&#39;https://devpost-challengepost.netdna-ssl.com/assets/defaults/no-avatar-100-17cf519ce6f8e4e0e83758ea09fc5eb3.png&#39;;" src="https://www.gravatar.com/avatar/b6cfd75473ae34088eaad669c442988e?d=https%3A%2F%2Fdevpost-challengepost.netdna-ssl.com%2Fassets%2Fdefaults%2Fno-avatar-180.png&amp;s=180" /></a>
        </div>
        <div class="media-content">
          <div class="input text required comment_body"><textarea class="text required" placeholder="Write a comment" name="comment[body]" id="comment_body">
</textarea></div>
          <input type="hidden" name="comment[location]" id="comment_location" value="project detail page" />
          <input type="submit" name="commit" value="Post comment" class="btn button radius small" />
        </div>
      </div>
    </div>
</form>
</section>

        </div>
      </div>

    </div>
    <div class="columns"></div>
  </div>
</article>

    </div>
  </div>
</article>









    </section>


  <footer id="devpost-footer">
  <div class="row">
    <div class="small-6 large-3 columns">
      <nav>
        <h4>Devpost</h4>
        <ul>
          <li><a href="https://info.devpost.com/about">About</a></li>
          <li><a href="https://info.devpost.com/careers">Careers</a></li>
          <li><a href="https://info.devpost.com/contact">Contact</a></li>
        </ul>
      </nav>
    </div>

    <div class="small-6 large-3 columns">
      <nav>
        <h4>Hackathons</h4>
        <ul>
          <li><a href="https://devpost.com/hackathons">Browse hackathons</a></li>
          <li><a href="https://devpost.com/software">Explore projects</a></li>
          <li><a href="https://help.devpost.com/">Help</a></li>
        </ul>
      </nav>
    </div>

    <hr class="clear show-for-small">

    <div class="small-6 large-3 columns">
      <nav>
        <h4>For Organizations</h4>
        <ul>
          <li><a href="https://post.devpost.com/hackathons">Host an in-person hackathon</a></li>
          <li><a href="https://post.devpost.com/online_hackathons">Host an online hackathon</a></li>
          <li><a href="https://post.devpost.com/app_contest_resources">Hackathon best practices</a></li>
        </ul>
      </nav>
    </div>

    <div class="small-6 large-3 columns">
      <nav>
        <h4>Connect</h4>
        <ul class="social-links">
          <li>
            <a href="https://twitter.com/devpost" target="_blank">
              <i class="fa fa-twitter-square"></i>
            </a>
          </li>
          <li>
            <a href="https://www.facebook.com/devposthacks" target="_blank">
              <i class="fa fa-facebook-square"></i>
            </a>
          </li>
          <li>
            <a href="https://www.youtube.com/playlist?list=PLmJ41elIxG7bRbhhCUQun3e4XNeyKc_-o" target="_blank">
              <i class="fa fa-youtube-square"></i>
            </a>
          </li>
        </ul>
      </nav>
    </div>

    <div class="small-6 large-12 columns">
      <nav id="site-footer-legal">
        <h4 class="show-for-small">Legal</h4>
        <ul>
          <li><a href="https://info.devpost.com/privacy"><small>Privacy policy</small></a></li>
          <li><a href="https://info.devpost.com/guidelines"><small>Community Guidelines</small></a></li>
          <li><a href="https://info.devpost.com/terms"><small>Terms of service</small></a></li>
        </ul>
      </nav>
    </div>
  </div>
</footer>



    <script src="https://devpost-challengepost.netdna-ssl.com/assets/reimagine2-b29abf2fa08ed2e58cf0057391d4c9f6.js"></script>
<script src="https://devpost-challengepost.netdna-ssl.com/assets/platform-84f453b50a566c166dff535dae1a94ac.js"></script>

<script src="https://devpost-challengepost.netdna-ssl.com/assets/home/home_application-ed15e1c1c2f3f506f03278f3e37101c9.js"></script>

<script type="text/javascript" charset="utf-8">
  (function() {
    mixpanel.identify("950598");
    mixpanel.register({"ref_feature":"portfolio","ref_content":"user-portfolio","ref_medium":"global-nav"});
  })();
</script>



  <script type="text/javascript">
  (function (d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s);
  js.id = id;
  js.src = "https://connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));
</script>

  <script type="text/javascript">
    (function (d, s, id) {
      var js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) return;
      js = d.createElement(s);
      js.id = id;
      js.src = "https://connect.facebook.net/en_US/sdk.js";
      fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'facebook-jssdk'));

    var addthis_config = {
      data_ga_property: "UA-2233558-21",
      ui_508_compliant: true,
      ui_use_addressbook: true,
      ui_email_note: "I thought you might be interested in Cookie Injection but with Real Cookies - What if we used a Cookie Monster and a cookie to represent HTTP request to teach cybersecurity to kids?. It was built with godot.",
      ui_email_from: "jakevossen@jakevossen.codes"
    };
    var addthis_share = {
      url_transforms: {
        shorten: {
          twitter: 'bitly'
        }
      },
      shorteners: {
        bitly: {}
      },
      email_template: "software_share_template",
      email_vars: {
        Title: "Cookie Injection but with Real Cookies",
        Subject: "Check out this project on Devpost",
        HomepageLink: "https://devpost.com/?utm_campaign=friends_share&utm_medium=email"
      },
      passthrough : {
        twitter: {
          via: "Devpost",
          text: "Check out Cookie Injection but with Real Cookies"
        },
        facebook: {
          app_id: 115745995110194,
          redirect_uri: "https://devpost.com/software/cookie-injection-but-with-real-cookies"
        }
      }
    };

    var DEVPOST_ADDTHIS = {
      show: function() {
        $('[data-add-this-buttons]').each(function() {$(this).removeClass("hide")});
      },
      hide: function() {
        $('[data-add-this-buttons]').each(function() {$(this).addClass("hide")});
      }
    }
  </script>



<script type="text/javascript" charset="utf-8">
  CP.env.addRoutes({
    follows_url: "https://devpost.com/follows",
    search_softwares_url: "https://devpost.com/software/search",
    new_software_url: "https://devpost.com/software/new",
    search_hackathons_url: "https://devpost.com/hackathons",
    notifications_url: "https://devpost.com/notifications",
    api: {
      users_url: "https://api.devpost.com/users"
    }
  })

  new Reimagine2();

  $(function onDocumentReady() {
      CP.Home.SoftwareCommentButton.setup();
  CP.Home.ArrowKeyGalleryNavigation.setup('#gallery');
  new CP.Home.EditableContribution('[data-contribution="editable-contribution"]')
  CP.Mn.app.HackathonPicker.start({
    software: {
      id: 206470,
      name: "Cookie Injection but with Real Cookies"
    }
  });
    CP.SingleSubmitForm.setup(".new_software_update")
  CP.Historic.setup(".software-updates");

  ventChannel().trigger("updates:list", "cookie-injection-but-with-real-cookies");
  CP.LinkCollectionTracker.setup(".recognized-tag a", "#app-details-right").track(
    "Tag Gallery",
    { "Tag displayed on": "software details page"}
  );
  new CP.Home.SoftwareLinks("[data-role=software-urls]").enhance();
  CP.Home.DismissableMessage.setup("[data-alert]");
  CP.ChallengeStateInfoTimeago.setup('#submissions, #draft-submissions');
    CP.platform.newsletterAlert();
  CP.SendFormOnCommandEnter.setup($("#masqueradee"));
  (function(inputs) {
    if (typeof inputs.cp_autocomplete === "function") inputs.cp_autocomplete();
    inputs.on('click', function(event) { return false; });
  })($("#masqueradee"));
  var FollowButtonApp = new CP.FollowButtonApp({
    user: {
      screen_name: "jakevossen",
      follow_through_id: 414459
  },
    urls: {
      register_url: "https://secure.devpost.com/users/register",
      user_follows_url: "https://devpost.com/jakevossen/follows",
      follow_through_url: "https://devpost.com/software_members/follows",
      follow_request_url: "https://devpost.com/follow_requests"
  },
  follow_through_scope: "software_member"
  });

  FollowButtonApp.start();
  var appOptions = {};

  _.extend(appOptions, {
    user: {
      id: 950598,
      display_name: "Jacob Vossen"
    }
  });

  CP.Mn.app.start(appOptions);

  });

</script>

<!--[if lt IE 9 ]>
  <script type="text/javascript">
    $(function onDocumentReady() {
      CP.IE.Notifications.setup();
    });
  </script>
<![endif]-->




<script type="application/ld+json">
{
    "@context": "http://schema.org",
    "@type": "WebSite",
    "url": "https://devpost.com/",
    "potentialAction": {
      "@type": "SearchAction",
      "target": "https://devpost.com/software/search?query={query}",
      "query-input": "name=query"
    }
}
</script>





<script type='text/javascript'>try {mixpanel.track("Logged In Pageview", {"time":1573351907,"ip":" 172.31.74.84","distinct_id":"950598","page_name":"home/softwares#show","orgs":[]});} catch(err) {};</script></body></html>
'''

@app.route('/')
def hello_world():
    return the_site

if __name__ == '__main__':
    app.run()
