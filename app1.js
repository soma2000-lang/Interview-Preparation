'use strict'

/**
 * Module dependencies.
 */

var express = require('../..');
var logger = require('morgan');
var path = require('path');
var session = require('express-session');
var methodOverride = require('method-override');

var app = module.exports = express();

// set our default template engine to "ejs"
// which prevents the need for using file extensions
app.set('view engine', 'ejs');

// set views for error and 404 pages
app.set('views', path.join(__dirname, 'views'));
app.response.message = function(msg){
    // reference `req.session` via the `this.req` reference
    var sess = this.req.session;
    // simply add the msg to an array for later
    sess.messages = sess.messages || [];
    sess.messages.push(msg);
    return this;
  };


if (!module.parent) app.use(logger('dev'));
// session support
app.use(session({
    resave: false, // don't save session if unmodified
    saveUninitialized: false, // don't create session until something stored
    secret: 'some secret here'
  }));

  // parse request bodies (req.body)
app.use(express.urlencoded({ extended: true }))