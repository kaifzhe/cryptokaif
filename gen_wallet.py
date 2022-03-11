import bip_utils, json, requests, telebot
from datetime import datetime

def getmnemonic():
    mnemonic = bip_utils.Bip39MnemonicGenerator().FromWordsNumber(bip_utils.Bip39WordsNum.WORDS_NUM_12)
    return mnemonic

def newaddr(currency, mnemonic):
    seed_bytes = bip_utils.Bip39SeedGenerator(mnemonic).Generate()
    bip44_mst_ctx = bip_utils.Bip44.FromSeed(seed_bytes, getattr(bip_utils.Bip44Coins, currency))
    bip44_acc_ctx = bip44_mst_ctx.Purpose().Coin().Account(0)
    bip44_chg_ctx = bip44_acc_ctx.Change(bip_utils.Bip44Changes.CHAIN_EXT)
    bip44_addr_ctx = bip44_chg_ctx.AddressIndex(0)
    bip44addr = bip44_addr_ctx.PublicKey().ToAddress()
    return bip44addr

def check_addr(address):
   balance = web3.eth.getBalance(address)
   balanceOf = web3.fromWei(balance, 'ether')
   return balanceOf

def send_msg(msg):
    bot = telebot.TeleBot('TG_BOT_TOKEN')
    bot.send_message(DIALOG_ID, msg)


def main():

  mnemonic = getmnemonic()
  
  pair_eth = newaddr('ETHEREUM', mnemonic)
  #pair_bsc = newaddr('BINANCE_SMART_CHAIN', mnemonic)
  
  total_cash_eth = check_addr(now_pair_eth)
  #total_cash_bsc = check_addr(now_pair_bsc)      
  
  send_msg(mnemonic, now_pair_eth, total_cash_eth)


