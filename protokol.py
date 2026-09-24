#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Uyku Devrimi Protokolü — çalışan ama kimsenin hayatını kurtarmayan ferman."""

from datetime import datetime

FERMAN_SAATI = 10  # öğleden önce ayakta durmak suçtur


def kac_dakika_daha(simdi: datetime) -> int:
    hedef = simdi.replace(hour=FERMAN_SAATI, minute=0, second=0, microsecond=0)
    if simdi >= hedef:
        return 0
    return int((hedef - simdi).total_seconds() // 60)


def ferman_bas():
    simdi = datetime.now()
    kalan = kac_dakika_daha(simdi)
    print("=" * 52)
    print("  UYKU DEVRİMİ PROTOKOLÜ — RESMİ FERMAN")
    print("=" * 52)
    print(f"Tarih-saat : {simdi.strftime('%d.%m.%Y %H:%M')}")
    print(f"Makam      : Yatak Başkanlığı")
    print()
    if kalan > 0:
        print(f"KARAR: Daha {kalan} dakika yorgan altında kalmanız tavsiye edilir.")
        print("Gerekçe: Sabah 10'dan önce ayakta durmak protokole aykırıdır.")
    else:
        print("KARAR: Yasal kalkış saati geçmiştir. Ayağa kalkabilirsiniz.")
        print("Uyari: Kalkış, çay demlenmeden gerçekleşirse geçersiz sayılır.")
    print()
    print("Yorgan tanıktır. Alarm ise sadece görüş bildirir.")
    print("=" * 52)
    # gizli not (siyasi değil, bürokrasi taşlaması):
    # c2VjaW0gbWFkZGU6IGJ1dHVuIHNpeWFzZXQgb3JiaXRyYWogYXluxaEgYXlsbmlrIGRla2lsCg==


if __name__ == "__main__":
    ferman_bas()
