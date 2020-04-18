/**
 * Z-MODAL
 * By Benjamin Caradeuc (benjamin@caradeuc.info)
 * benavern.github.io
 */

(function() {

  // constructor
  this.ZMODAL = function() {
    // global element
    this.closeBtn = null;
    this.modal = null;
    this.btns = [];
    // defaults options
    var defaults = {
      className : "",
      title : "Z-MODAL",
      content : '<h1>Congratulations!!!</h1>\
          <p>You are using the realy awesome Z-Modal javascript plugin. <b>Thank You!</b></p>\
          <p>Author: <a href="http://caradeuc.info/">Benjamin Caradeuc</a></p>',
	  showOverlay: true,
      autoload:true,
	  closeBtn : true,
	  onClose:null,
      buttons : [
          { label: "ok", className: '', half: false, closeOnClick: true, callback:function() { console.log('Thank you for using Z-Modal plugin.'); } }
      ]
    }

    if(arguments[0] && typeof arguments[0] === "object"){
      this.options = __createOptions(defaults, arguments[0]);
    }else{
      this.options = defaults;
    }
    if(this.options.autoload === true){
      this.open.call(this);
    }
  }


  /*============================================================================
   fonctions privées
  */

  // create the options object
  function __createOptions(defaults, props){
    var opt = defaults; // the options to return
    for (var prop in props){
      if (props.hasOwnProperty(prop)) {
        opt[prop] = props[prop];
      }
    }
    return opt;
  }

  // build the html markup
  function __build() {
    /**
     * If content is a string, append it.
     * If content is a Dome node, append its content.
     */
    var theContent;
        _this = this;;
    if (typeof this.options.content === "string") {
      theContent = this.options.content;
    } else if (!!this.options.content){ //content isn't a falsy value @http://bit.do/js-falsy-values
      theContent = this.options.content.innerHTML;
    } else {
		theContent = "";
	}
    // modal element creation
    this.modal = document.createElement("div");
    this.modal.className = "z-modal " + this.options.className;
	if(this.options.showOverlay){
		__initListener(this.modal, "click", function (){
		  _this.close.call(_this);
		}, true);
		this.modal.classList.add("overlay");
	}
	
    // the box
    var box = document.createElement("div");
    box.className = "z-modal-box";
    this.modal.appendChild(box);

	if(!!this.options.title){ //title isn't a falsy value @http://bit.do/js-falsy-values
	    // the box header (title - closeBtn)
		var header = document.createElement("div");
		header.className = "z-modal-header";
		
		// title
		var title = document.createElement("div");
		title.className = "z-modal-title";
		title.innerHTML = this.options.title;
		header.appendChild(title);

        // closeBtn
	    if (!!this.options.closeBtn) { //isn't a falsy value @http://bit.do/js-falsy-values
	        this.closeBtn = document.createElement("div");
	        this.closeBtn.className = "z-modal-close";
	        this.closeBtn.innerHTML = "&#215;";
	        __initListener(this.closeBtn, "click", function() {
	            _this.close.call(_this);
	        });
	        header.appendChild(this.closeBtn)
	    }

	    // append to box
		box.appendChild(header);
	}
	 
	if(!!theContent){ //theContent isn't a falsy value @http://bit.do/js-falsy-values
		// the box content
		var content = document.createElement("div");
		content.className="z-modal-content";
		content.innerHTML = theContent;
		// append to box
		box.appendChild(content);
	}
	
	if(this.options.buttons.length){
		// the box footer
		var footer = document.createElement("div");
		footer.className="z-modal-footer";
		// the buttons
		for(var i=0; i<this.options.buttons.length; i++){
		  // closure...
		  (function(i) {
			var theBtn = _this.options.buttons[i];
			var btn = document.createElement("button");
			btn.className = "z-modal-btn";
			if(theBtn.className && theBtn.className.length > 0)
				btn.classList.add(theBtn.className);
			btn.innerHTML = theBtn.label;
			if(theBtn.half === true){
			  btn.classList.add("z-modal-btn-half");
			}
			// listeners
            __initListener(btn, "click", function () {
                if (theBtn.closeOnClick === false) {
                    theBtn.callback();
                } else {
                    _this.close.call(_this, theBtn.callback);
                }
			})
			footer.appendChild(btn);
		  })(i);
		}
		// append to box
		box.appendChild(footer);
	}

    // add the modal to the dom ! finally!
    document.body.appendChild(this.modal)

  }

  function __initListener(node, type, func, noDeep){
    var _this = this;
    node.addEventListener(type, function(e) {
      // e.preventDefault();
      if(noDeep === true){
        if(e.target == this){
          func();
        }
      }
      else{
        func();
      }
    }, false);
  }


  /*============================================================================
   fonctions publiques
  */

  // open the modal (create it before ...)
  this.ZMODAL.prototype.open = function() {
	if (ZMODAL.__instance) return ZMODAL.__instance;
	__build.call(this);
	ZMODAL.__instance = this;
  }

  // close the modal (and delete it ...)
  this.ZMODAL.prototype.close = function(callback) {
	if (!ZMODAL.__instance) return null;
    // execute the callback function...
    if(typeof callback === 'function'){
      callback();
    } else if(typeof this.options.onClose === 'function'){
      this.options.onClose();
	}	  
	  
	ZMODAL.__instance = null;  
	  
    // remove the modal
     this.modal.parentNode.removeChild(this.modal);
  }

}());
