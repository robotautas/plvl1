# Tuples

Tuplas yra nekintama iteruojama duomenų struktūra python'e.

```python
savaite = ('pirmadienis', 'antradienis', 'treciadienis', 'ketvirtadienis', 'penktadienis', 'sestadienis', 'sekmadienis')

print(savaite)
print(type(savaite))

#('pirmadienis', 'antradienis', 'treciadienis', 'ketvirtadienis', 'penktadienis', 'sestadienis', 'sekmadienis')
#<class 'tuple'>
```

tuplas koks deklaruojamas, toks ir išlieka visą laiką:

```python
savaite.append('astuntadienis')
# AttributeError: 'tuple' object has no attribute 'append'
```

```python
savaite[0] = 'kitadienis'
# 'tuple' object does not support item assignment
```

## Tuple'ų privalumai:
* Veikia greičiau už listus
* Tam tikrose situacijose užtikrina saugumą
* Galima naudoti kaip raktus žodyne

```python
coords = {
    (54.677778, 25.291667): 'Vilnius',
    (54.897222, 23.886111): 'Kaunas'   
}
```
## Iteracija

Iteruoti per tuple'us galima taip pat, kaip ir per sąrašus:

```python
for diena in savaite:
    print(diena)

# pirmadienis
# antradienis
# treciadienis
# ketvirtadienis
# penktadienis
# sestadienis
# sekmadienis
```

taip pat veikia ir indeksacija bei pjūviai:

```python
print(savaite[1])
print(savaite[0:2])

# antradienis
# ('pirmadienis', 'antradienis')
```

## Tuple'ų metodai:

.count():
```python
x = (1,2,3,3,3,3)

print(x.count(2)) #1 
print(x.count(3)) #4
```

.index():
```python
print(x.index(2)) #1
print(x.index(3)) #2
```


