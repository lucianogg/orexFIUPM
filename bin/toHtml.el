#!/usr/bin/emacs --script
;;; exportToHTML --- asdasdasd
;;; Commentary:


;;; Code:
;;;(defvar infile "~/Dropbox/actualesUPM/beca/orexFIUPM/acbilaterales1819.org")
;;;(defvar outfile (file-truename (or "~/Dropbox/actualesUPM/beca/orexFIUPM/exports/acbilaterales1819.html" (replace-regexp-in-string "\.org$" ".html" infile))))

(defvar infile (getenv "infile"))
(defvar outfile (file-truename (getenv "outfile")))

;; remember the current directory; find-file changes it
(defvar cwd default-directory)
;; copy the source file to a temporary file; note that using the
;; infile as the base name defines the working directory as the same
;; as the input file
(defvar infile-temp (make-temp-name (format "%s.temp." infile)))
(copy-file infile infile-temp t)
(find-file infile-temp)
(org-mode)
(org-html-export-as-html)
(write-file outfile)

;; clean up
(setq default-directory cwd)
(delete-file infile-temp)
