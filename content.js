(function () {
  'use strict';

  function isEditableTarget(el) {
    if (!el) return false;
    if (el.tagName === 'TEXTAREA') return true;
    if (el.getAttribute && el.getAttribute('contenteditable') === 'true') return true;
    return false;
  }

  function insertLineBreak() {
    if (document.execCommand && document.execCommand('insertLineBreak')) {
      return;
    }
    const sel = window.getSelection();
    if (!sel || sel.rangeCount === 0) return;
    const range = sel.getRangeAt(0);
    range.deleteContents();
    const br = document.createElement('br');
    range.insertNode(br);
    range.setStartAfter(br);
    range.setEndAfter(br);
    sel.removeAllRanges();
    sel.addRange(range);
  }

  document.addEventListener(
    'keydown',
    function (e) {
      if (e.key !== 'Enter') return;
      if (e.isComposing || e.keyCode === 229) return;
      if (!isEditableTarget(e.target)) return;

      e.stopImmediatePropagation();
      e.preventDefault();
      insertLineBreak();
    },
    true
  );
})();
