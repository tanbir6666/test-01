(function ()
{
    function n(a, b) { try { h.test(b) && this.addEventListener("loadend", p.bind(this)) } catch (c) { } return e.apply(this, arguments) } function p() { try { var a = this.getResponseHeader("X-IDM-Request-ID"); a && g([1229212979, a, k.test(this.responseText) && this.responseText || null], "/") } catch (b) { } } function q(a, b) { var c = f.apply(this, arguments); try { if (h.test(a.url || a)) return c.then(r) } catch (d) { } return c } function r(a)
    {
        try
        {
            var b = a.headers.get("X-IDM-Request-ID"); if (b) if (a.ok)
            {
                var c = a.text, d = a.json; a.text = function ()
                {
                    return c.call(this).then(l.bind(null,
                        b, !1))
                }; a.json = function () { return d.call(this).then(l.bind(null, b, !0)) }
            } else g([1229212979, b], "/")
        } catch (m) { } return a
    } function l(a, b, c) { try { var d = b ? JSON.stringify(c) : c; g([1229212979, a, k.test(d) && d || null], "/") } catch (m) { } return c } const t = window.origin || document.origin || location.origin, g = window.postMessage.bind(window), u = Array.isArray; var h, k, e, f; window.addEventListener("message", function (a)
    {
        var b = a.data; if (u(b) && a.origin == t) switch (b[0])
            {
                case 1229212978: a = b[1]; var c = b[2], d = b[3]; b = b[4]; d ? (h = RegExp(d),
                    k = RegExp(b)) : a = c = !1; try { a ? e || (e = XMLHttpRequest.prototype.open) && (XMLHttpRequest.prototype.open = n) : e && (XMLHttpRequest.prototype.open = e, e = null), c ? f || (f = fetch) && (fetch = q) : f && (fetch = f, f = null) } catch (m) { }
            }
    }, !1); g([1229212977], "/")
})();
