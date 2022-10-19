document.addEventListener("DOMContentLoaded", function (event) {
  const useDarkMode = window.matchMedia("(prefers-color-scheme: dark)").matches;

  let sc = document.createElement("script");
  sc.setAttribute(
    "src",
    "https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js"
  );
  document.head.appendChild(sc);
  sc.onload = () => {
    tinymce.init({
      selector: "#id_description",
      skin: "oxide",
      width: 1000,
      height: 600,
      skin: useDarkMode ? "oxide-dark" : "oxide",
      content_css: useDarkMode ? "dark" : "default",
      plugins:
        "preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap pagebreak nonbreaking anchor tableofcontents insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker editimage help formatpainter permanentpen pageembed charmap tinycomments mentions quickbars linkchecker emoticons advtable export footnotes mergetags autocorrect",
      mobile: {
        plugins:
          "preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap pagebreak nonbreaking anchor tableofcontents insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker help formatpainter pageembed charmap mentions quickbars linkchecker emoticons advtable footnotes mergetags autocorrect",
      },
      toolbar:
        "undo redo | bold italic underline strikethrough | fontfamily fontsize blocks | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment | footnotes | mergetags",
      quickbars_selection_toolbar:
        "bold italic | quicklink h2 h3 blockquote quickimage quicktable",
      spellchecker_ignore_list: ["Ephox", "Moxiecode"],
      autocorrect_capitalize: true,
      toolbar_mode: "sliding",
      tinycomments_mode: "embedded",
      image_caption: true,
      noneditable_class: "mceNonEditable",
      content_style: ".mymention{ color: gray; }",
      contextmenu: "link image editimage table configurepermanentpen",
      a11y_advanced_options: true,
      menu: {
        tc: {
          title: "Comments",
          items: "addcomment showcomments deleteallconversations",
        },
        favs: {
          title: "My Favorites",
          items: "code visualaid | searchreplace | emoticons",
        },
      },
      menubar: "favs file edit view insert format tools table help",
      content_css: "css/content.css",
    });
  };
});

/* tinymce.init({
     selector: "#id_description",

     menubar: "file edit view insert format tools table tc help",
    
     
     height: 600,
     image_caption: true,
     ,

   });*/
