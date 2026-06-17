# Tkinter no renderiza imágenes (PNG/GIF)

**Fecha:** 2026-06-17 · **Contexto:** `stanfordpy.graphics` en `CSBridge/2026/water-demo.py`

**Ubicación del bug:** `C:\Program Files\Python312\Lib\site-packages\stanfordpy\graphics\graphics.py`
- función `create_image` → **línea 314**
- función `create_image_with_size` → **líneas 344-346**

## 🇪🇸 Español

**Síntoma:** la imagen no aparece; queda un espacio en blanco aunque el objeto se crea.

**Causa:** el `PhotoImage` se crea en línea y nadie guarda referencia, así que Python lo borra (garbage collection). El canvas solo lo enlaza débilmente.

```python
# graphics.py:314 — el bug
object_id = self.canvas.create_image(x, y, image=tk.PhotoImage(file=filePath))
```

**Solución:** guardar una referencia. En `graphics.py`:

```python
# 1. en __init__ (~línea 61):
self._images = []

# 2. en create_image (314) y create_image_with_size (344):
photo = tk.PhotoImage(file=filePath)
self._images.append(photo)          # referencia fuerte → no se borra
object_id = self.canvas.create_image(x, y, image=photo)
```

**⚠️ Consecuencia del hotfix:** la imagen **sí carga**, pero se dibuja a su **tamaño nativo en píxeles**, no ajustada al canvas. `tk.Canvas.create_image` **ignora** `width`/`height` (por eso `create_image_with_size` tampoco escala). Si la imagen es más grande que el canvas, se desborda o se recorta. Para que encaje hay que **redimensionar el archivo antes** o escalarlo con Pillow (`Image.resize` + `ImageTk.PhotoImage`).

**Sobre PNG:** Python 3.12 trae Tk 8.6, que sí soporta PNG. Si da error `couldn't recognize data in image file`, el archivo no es PNG real (p. ej. un JPEG renombrado) → usa Pillow.

---

## 🇬🇧 English

**Symptom:** the image doesn't show; you get a blank space even though the object is created.

**Cause:** the `PhotoImage` is created inline with no reference kept, so Python garbage-collects it. The canvas only links to it weakly.

```python
# graphics.py:314 — the bug
object_id = self.canvas.create_image(x, y, image=tk.PhotoImage(file=filePath))
```

**Fix:** keep a reference. In `graphics.py`:

```python
# 1. in __init__ (~line 61):
self._images = []

# 2. in create_image (314) and create_image_with_size (344):
photo = tk.PhotoImage(file=filePath)
self._images.append(photo)          # strong reference → not collected
object_id = self.canvas.create_image(x, y, image=photo)
```

**⚠️ Hotfix consequence:** the image **does load**, but it's drawn at its **native pixel size**, not fitted to the canvas. `tk.Canvas.create_image` **ignores** `width`/`height` (that's why `create_image_with_size` doesn't scale either). If the image is bigger than the canvas, it overflows or gets clipped. To make it fit, **resize the file beforehand** or scale it with Pillow (`Image.resize` + `ImageTk.PhotoImage`).

**About PNG:** Python 3.12 ships Tk 8.6, which supports PNG. If you get `couldn't recognize data in image file`, the file isn't a real PNG (e.g. a renamed JPEG) → use Pillow.
