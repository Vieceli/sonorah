

// Prevents the enter key from submitting a form; acts as a tab instead
// As seen on stackoverflow: http://stackoverflow.com/questions/1563062/jquery-prevent-form-submition-with-enter-key
function preventEnterSubmit(e) 
{
  if (e.which == 13)  {

    var tgt = $(e.target);

    if (!tgt.is("textarea,:button,:submit,:file"))  {

      var focusNext = false;
      $(this.form).find(":input:visible:not([disabled],[readonly],[tabIndex=-1])").each(function(){
        if (this === e.target) {
          $(this).blur();
          focusNext = true;
        }
        else if (focusNext){
          $(this).focus();
          return false;
        }
      });

      return false;
    }
  }
}

function showTip(element, msg, cfg)
{
  var cfg = cfg || {};
  var o = { 
    content: msg,
    style: { 
      name: cfg.styleName || 'cream', 
      tip: cfg.styleTip || 'leftMiddle', 
      color: 'white',
      border: { width: 1, radius: 1 },
      width: { max: 400 }
    }, 
    show: { when: { event: cfg.showEvent || 'focus' }, ready: cfg.showReady || false }, 
    hide: { when: { event: cfg.hideEvent || 'blur' } }, 
    position: { corner: { target: cfg.targetPosition || 'rightMiddle', tooltip: cfg.tooltipPosition || 'leftMiddle' } } 
  };
  if(cfg.destroy) o.api = { onHide: function(event) { $(event.target).qtip('destroy'); } };
  $(element).qtip(o);
}

function showHint(element, msg)
{
  $(element).Watermark(msg);
  //return showTip(element, msg);
}

function showError(element, msg, immediate)
{
  showReady = immediate ? true : false;
  return showTip(element, msg, { styleName: 'red', showReady: showReady, destroy: true });
}



