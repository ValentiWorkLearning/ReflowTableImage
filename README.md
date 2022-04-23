## Build
```shell
make BR2_EXTERNAL=${REPO_ROOT} -C buildroot O=${REPO_ROOT}/image_build/ orange_table_defconfig
```
## DTS Spi overlay
```dts
&spi1 {
	status = "okay";

        temp-sensor@1 {
            compatible = "maxim,max6675";
            reg = <0>;
            spi-max-frequency = <4300000>;
            spi-cpha;
        };

};
```


## Boot from NFS:
Device console:
```shell
setenv bootargs console=${console} root=/dev/nfs rootfstype=nfs ip=dhcp nfsvers=3 nfsroot=192.168.0.126:/nfs/orange_zero_rootfs
run bootargs
```

Completed image build:
## Example
```shell
sudo tar -xavf /path/to/output_dir/rootfs.tar -C /path/to/nfs_root_dir
```

## Host PC
```shell
cd images
sudo tar -xavf rootfs.tar -C /mnt/orange_zero_rootfs/
cd ..
```


## TFTP:
https://www.emcraft.com/som/stm32mp1/loading-linux-images-via-ethernet-and-tftp

### U-Boot console TFTP boot
```shell
setenv serverip 192.168.0.126

setenv ipaddr 192.168.0.116

setenv image zImage

setenv dtbimage sun8i-h2-plus-orangepi-zero.dtb

setenv bootargs root=/dev/nfs rw nfsroot=${serverip}:/mnt/rootfs/,nfsvers=3,tcp ip=${ipaddr}:${serverip}::255.255.255.0::eth0:any::8.8.8.8:

setenv netboot 'tftp ${kernel_addr_r} ${image} && tftp ${fdt_addr_r} ${dtbimage} && bootz ${kernel_addr_r} - ${fdt_addr_r}'

run netboot
```
### Linux Kernel Doc
https://www.kernel.org/doc/Documentation/filesystems/nfs/nfsroot.txt


```shell
setenv bootargs "root=/dev/nfs ro nfsroot=${serverip}:/srv/nfs/,nfsvers=3,tcp ip=${ipaddr}:${serverip}:10.0.200.1:255.255.255.0:kontron:eth0:any:10.0.200.1:8.8.8.8:";

bootz ${kernel_addr_r} - ${fdt_addr_r}
```

## Mounting NFS
mount -o port=2049,nolock,proto=tcp 192.168.0.126:/mnt/hostname  /mnt/target_name

Don't forget about the /etc/export file

```shell
/srv/nfs/ *(rw,no_subtree_check,sync,no_root_squash,no_all_squash)
```