import os
import time
from functools import wraps
from io import BytesIO
from flask_mail import Message
from werkzeug.security import generate_password_hash
from app.apps import db, mail
from app.admin import admin
from flask import render_template, make_response, session, redirect, url_for, request, flash, abort
from app.admin.forms import LoginForm, RegisterForm, addsuppliers, increasePurchaseOrders, purchsearch, \
    returnordersearch, goodssearch, addgoodsname, suppliersserach, salesorderssearch, returnsalessearch, customesserch, \
    addcustomes, warehouseserch, enteringwarehouseserach, outWarehousingsearch, \
    addsection, adddutys, powerss, addsaleorder, bumens, alertpasswd, wjpasswd, beifenser
from app.admin.uilt import get_verify_code, bars, lines, pies, on_created
from app.models import User, Purchase, goods, supplier, client, section, duty, inwarehouse, stock, sealreturngoods, \
    warehouse, returngoods, sales, power


users = User.query.filter_by(user_id='1').first()
# users.user_duty = form.data['dutyser']
# 根据form.data['dutyser']去查询duty表中的duty_name
users.user_duty = duty.query.filter_by(duty_id='1').first().duty_name
print(users.user_duty)
# users.user_section = form.data['sectionsr']
# users.user_section = section.query.filter_by(section_id='3').first()
a = section.query.filter_by(section_id='3').first().section_name
print(a)
